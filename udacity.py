import webapp2

form="""
<form method="get" action="/testform">
    <select name="q">
	<option value="1">one</option>
	<option value="2">two</option>
	<option value="3">three</option>
    </select>
    <input type="submit" />
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
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(self.request)
        self.response.write("<br /><a href=\"/\">/</a>")

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler),
], debug=True)
