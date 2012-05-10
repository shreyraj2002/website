#Base Page Handlers
import tornado.web
import forms


class AboutHandler(tornado.web.RequestHandler):
    ''' About Page Handler '''
    def get(self):
        form = forms.HelloForm()
        self.render('about.html', form=form)

    def post(self):
        form = forms.HelloForm(self)
        if form.validate():
            self.write('Hello %s' % form.planet.data)
        else:
            self.render('about.html', form=form)


class CodeHandler(tornado.web.RequestHandler):
    ''' Code Page Handler '''
    def get(self):
        form = forms.HelloForm()
        self.render('code.html', form=form)

    def post(self):
        form = forms.HelloForm(self)
        if form.validate():
            self.write('Hello %s' % form.planet.data)
        else:
            self.render('code.html', form=form)


class ResumeHandler(tornado.web.RequestHandler):
    ''' Resume Page Handler '''
    def get(self):
        form = forms.HelloForm()
        self.render('resume.html', form=form)

    def post(self):
        form = forms.HelloForm(self)
        if form.validate():
            self.write('Hello %s' % form.planet.data)
        else:
            self.render('resume.html', form=form)
