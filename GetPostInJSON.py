import webapp2
import json
from Post import Post
from google.appengine.ext import ndb

class GetPostInJSON(webapp2.RequestHandler):
    def get(self):
        uri = self.request.uri
        uri = uri.split('/')
        postid = uri[len(uri)-1]
        postid = int(postid[:-5])

        post = Post.get_by_id(postid)
        #post = ndb.gql('SELECT * FROM Post WHERE ID=:1', postid).get()

        json_post = dict()

        json_post["subject"] = post.subject
        json_post["content"] = post.content

        self.response.headers['Content-Type'] = "application/json"
        self.response.out.write(json.dumps(json_post))
