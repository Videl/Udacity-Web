import webapp2
from Post import Post
import jinja2
import os


jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class WelcomePage(webapp2.RequestHandler):
    def get(self):
        query = Post.query() # retrieve all account entities

        posts = query.fetch()

        values = {
                'posts': posts
        }

        template = jinja_environment.get_template('home.Jinja2')
        self.response.out.write(template.render(values))
