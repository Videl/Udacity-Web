import webapp2
import re

form = """
<h1>Signup</h1>
<form method="post" action="/">
    <dl>
	<dt>Username</dt>
	    <dd><input type="text" name="username" value="%(past_username)s" /> %(username)s</dd>
	<dt>Password</dt>
	    <dd><input type="password" name="password" /> %(password)s</dd>
	<dt>Verify Password</dt>
	    <dd><input type="password" name="verify" />  %(verify)s</dd>
	<dt>Mail (optional)</dt>
	    <dd><input type="text" name="email" /> %(mail)s</dd>
    </dl>

    <input type="submit" />
</form>
"""


class MainPage(webapp2.RequestHandler):
    def write_form(self, past_username="",
                   username="",
                   password="",
                   verify="",
                   mail=""):
        self.response.write(
            form % {"past_username": past_username,
                    "username": username,
                    "password": password,
                    "verify": verify,
                    "mail": mail
            })

    def get(self):
        self.write_form()

    def post(self):
        # Let's check!
        input_username = self.request.get("username")
        input_pass = self.request.get("password")
        input_verify = self.request.get("verify")
        input_mail = self.request.get("email")

        regex_user = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        regex_pass = re.compile("^.{3,20}$")
        regex_mail = re.compile("^[\S]+@[\S]+\.[\S]+$")

        error = False

        message_username = ""
        message_pass = ""
        message_verify = ""
        message_mail = ""

        if input_username and input_pass and input_verify:
            if not regex_user.match(input_username):
                message_username = "That's not a valid username."
                error = True

            if not regex_pass.match(input_pass):
                message_pass = "That's not a valid password."
                error = True

            if input_verify != input_pass:
                message_verify = "Your passwords didn't match."
                error = True

            if input_mail:
                if not regex_mail.match(input_mail):
                    message_mail = "That's not a valid email."
                    error = True
        else:
            if not input_username:
                message_username = "Please enter all fields."
            if not input_pass:
                message_pass = "Please enter all fields."
            if not input_verify:
                message_verify = "Please enter all fields."
            if not input_mail:
                message_mail = "Please enter all fields."
            error = True

        if error:
            self.write_form(input_username,
                            message_username,
                            message_pass,
                            message_verify,
                            message_mail)
        else:
            self.response.headers.add_header("Set-Cookie", "username=%s" % str(input_username))
            self.redirect("/welcome")


class WelcomePage(webapp2.RequestHandler):
    def get(self):
        username = self.request.cookies.get("username", None)
        if username:
            self.response.write("<h1>Welcome, " + username + "!")
        else:
            self.redirect("/")


application = webapp2.WSGIApplication([
                                          ('/', MainPage),
                                          ('/welcome', WelcomePage),
                                      ], debug=True)

