import webapp2
import os
import jinja2
from GetPostInJSON import GetPostInJSON


from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Post(ndb.Model):
    subject = ndb.StringProperty(indexed=True)
    content = ndb.StringProperty(indexed=False)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        query = Post.query() # retrieve all account entities

        posts = query.fetch()

        values = {
                'posts': posts
        }

        template = jinja_environment.get_template('home.Jinja2')
        self.response.out.write(template.render(values))

class GetPost(webapp2.RequestHandler):
    def get(self):
        uri = self.request.uri
        uri = uri.split('/')
        postid = int(uri[len(uri)-1])

        post = Post.get_by_id(postid)
        # post = ndb.gql('SELECT * FROM Post WHERE ID=:1', postid).get()

        values = {
                'post': post
        }

        template = jinja_environment.get_template('post.Jinja2')
        self.response.out.write(template.render(values))


class SubmitPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('submit_form.Jinja2')
        values = {
                'subject':"",
                'content':"",
                'error':"All fields needs text."
        }
        self.response.out.write(template.render(values))

    def post(self):
        values = {
                'subject':"",
                'content':"",
                'error':""
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


application = webapp2.WSGIApplication([
    ('/blog', WelcomePage),
    ('/blog/newpost', SubmitPage),
    ('/blog/[0-9]*', GetPost),
    ('/blog/[0-9]*\.json$', GetPostInJSON),
], debug=True)

