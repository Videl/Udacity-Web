import webapp2

from LoginPage import LoginPage
from LogoutPage import LogoutPage
from GetPostInJSON import GetPostInJSON
from SubmitPage import SubmitPage
from GetPost import GetPost
from WelcomePageInJSON import WelcomePageInJSON
from WelcomePage import WelcomePage
from SignupPage import MainPage
from LoginWelcome import LoginWelcome

application = webapp2.WSGIApplication([
    ('/blog', WelcomePage),
    ('/blog.json', WelcomePageInJSON),
    ('/blog/newpost', SubmitPage),
    ('/blog/[0-9]*', GetPost),
    ('/blog/[0-9]*\.json$', GetPostInJSON),
    ('/blog/signup', MainPage),
    ('/blog/welcome', LoginWelcome),
    ('/blog/login', LoginPage),
    ('/blog/logout', LogoutPage),
], debug=True)


