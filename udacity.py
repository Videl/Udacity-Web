import webapp2
import rot13

form="""
<form method="post" action="/">
    <p>Enter some text to ROT13:</p>
<textarea name="text">%(message)s</textarea>
    <br />
    <input type="submit" />
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, message = ""):
	self.response.out.write(form % {"message": message})

    def get(self):
        self.write_form()
        
    def post(self):
	source = self.request.get("text")
	transformed = rot13.parse(source)
	self.write_form(transformed)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
