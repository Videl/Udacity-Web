import webapp2

form="""
<form action="/testform">
    <input name="q" />
    <input type="submit"
</form>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):

    def get(self):
	request = self.request.get("q")
        self.response.write(request)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler),
], debug=True)
