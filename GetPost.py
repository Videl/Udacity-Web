import webapp2
from Post import Post
import jinja2
import os


jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))



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
