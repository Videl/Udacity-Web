import webapp2
from Post import Post
import json


class WelcomePageInJSON(webapp2.RequestHandler):
    def get(self):
        query = Post.query() # retrieve all account entities

        posts = query.fetch()

        post_list = list()

        for post in posts:
            json_post = dict()
            json_post["subject"] = post.subject
            json_post["content"] = post.content
            post_list.append(json_post)

        self.response.headers['Content-Type'] = "application/json"
        self.response.out.write(json.dumps(post_list))