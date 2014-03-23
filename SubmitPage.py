import webapp2
from Post import Post
import jinja2
import os


jinja_environment = jinja2.Environment(autoescape=True,
                                       loader=jinja2.FileSystemLoader(
                                           os.path.join(os.path.dirname(__file__), 'templates')))


class SubmitPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('submit_form.Jinja2')
        values = {
            'subject': "",
            'content': "",
            'error': "All fields needs text."
        }
        self.response.out.write(template.render(values))

    def post(self):
        values = {
            'subject': "",
            'content': "",
            'error': ""
        }

        values['subject'] = self.request.get("subject")
        values['content'] = self.request.get("content")

        if values['subject'] and values['content']:
            post_name = values['subject']
            post = Post()

            post.subject = values['subject']
            post.content = values['content']
            post.put()

            self.redirect('/blog/' + str(post.key.id()))
        else:
            values['error'] = "Please enter all fields, noob."

        template = jinja_environment.get_template('submit_form.Jinja2')
        self.response.out.write(template.render(values))

