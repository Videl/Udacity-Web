import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class SubmitPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('submit_form.Jinja2')
        self.response.out.write(template.render(template_values))

    def post(self):
        form = web.input(subject, content)

        self.reponse.out.write("Coucou")

application = webapp2.WSGIApplication([
    ('/blog/newpost', SubmitPage),

], debug=True)

