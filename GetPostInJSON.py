import webapp2

class GetPostInJSON(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Tentative de choper du JSON!")
