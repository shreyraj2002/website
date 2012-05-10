#Blog Handlers
import tornado.web
import forms


class BlogHandler(tornado.web.RequestHandler):
    ''' Blog Handler '''
    def get(self):
        form = forms.HelloForm()
        self.render('blog.html', form=form)

    def post(self):
        form = forms.HelloForm(self)
        if form.validate():
            self.write('Hello %s' % form.planet.data)
        else:
            self.render('blog.html', form=form)
