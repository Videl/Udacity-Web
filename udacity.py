import webapp2

form="""
<form method="post" action="/">
    <input type="text" name="q" />
    <input type="submit" />
    <div>%(message)s</div>
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, message = ""):
	self.response.out.write(form % {"message": message})

    def get(self):
        self.write_form()
        
    def post(self):
	entered = self.request.get("q")
	self.write_form(entered)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
