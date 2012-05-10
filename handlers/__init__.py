#Python Imports
import os

# Tornado imports
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from tornado.web import url

# Sqlalchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#Handler Imports
from handlers.blog import BlogHandler
from handlers.base import AboutHandler, CodeHandler, ResumeHandler

import forms
import uimodules
import models

# Options
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, type=bool)
define("db_path", default='sqlite:///db/storage.db', type=str)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
          url(r'/', IndexHandler, name='index'),
          url(r'/index', IndexHandler, name='index2'),
          url(r'/about', AboutHandler, name='about'),
          url(r'/code', CodeHandler, name='code'),
          url(r'/resume', ResumeHandler, name='resume'),
          url(r'/blog', BlogHandler, name='blog'),
        ]
        settings = dict(
          debug=options.debug,
          static_path=os.path.join(os.path.dirname(__file__), "../static"),
          template_path=os.path.join(os.path.dirname(__file__), '../views'),
          xsrf_cookies=True,
          # TODO Change this to a random string
          cookie_secret="nzjxcjasduuqwheazmu293nsadhaslzkci9023nsadnua9sdads/Vo=",
          ui_modules=uimodules,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        engine = create_engine(options.db_path, convert_unicode=True, echo=options.debug)
        models.init_db(engine)
        self.db = scoped_session(sessionmaker(bind=engine))


# Custom Error Handler

class ErrorHandler(tornado.web.RequestHandler):
    """Generates an error response with status_code for all requests."""
    def __init__(self, application, request, status_code):
        tornado.web.RequestHandler.__init__(self, application, request)
        self.set_status(status_code)

    def get_error_html(self, status_code, **kwargs):
        if status_code == 404:
            return self.render('404.html')
        elif status_code == 405:
            return self.render_string('methodnotfound.html')
        elif status_code == 500:
            return self.render_string('servererror.html')

    def prepare(self):
        raise tornado.web.HTTPError(self._status_code)

## override the tornado.web.ErrorHandler with our default ErrorHandler
tornado.web.ErrorHandler = ErrorHandler


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class IndexHandler(BaseHandler):
    def get(self):
        form = forms.HelloForm()
        self.render('index.html', form=form)

    def post(self):
        form = forms.HelloForm(self)
        if form.validate():
            self.write('Hello %s' % form.planet.data)
        else:
            self.render('index.html', form=form)
