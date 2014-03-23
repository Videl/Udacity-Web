import webapp2
from User import User

class LoginWelcome(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.cookies.get("user_id", None)

        if user_id:
            user = User.get_by_id(int(user_id))

            if user:
                self.response.out.write("<h1>Welcome, %s !</h1>" % user.username)
            else:
                self.redirect("/signup")
        else:
                self.redirect("/signup")