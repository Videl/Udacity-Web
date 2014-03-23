import webapp2
from GetPostInJSON import GetPostInJSON
from SubmitPage import SubmitPage
from GetPost import GetPost
from WelcomePageInJSON import WelcomePageInJSON
from WelcomePage import WelcomePage

application = webapp2.WSGIApplication([
    ('/blog', WelcomePage),
    ('/blog.json', WelcomePageInJSON),
    ('/blog/newpost', SubmitPage),
    ('/blog/[0-9]*', GetPost),
    ('/blog/[0-9]*\.json$', GetPostInJSON),
], debug=True)

