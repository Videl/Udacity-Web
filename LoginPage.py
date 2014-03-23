import webapp2
from User import User

form = """
<h1>Signup</h1>
<form method="post" action="/login">
    <dl>
	<dt>Username</dt>
	    <dd><input type="text" name="username" value="%(past_username)s" /> %(username)s</dd>
	<dt>Password</dt>
	    <dd><input type="password" name="password" /> %(password)s</dd>
    </dl>

    <input type="submit" />
</form>
"""


class LoginPage(webapp2.RequestHandler):
    def write_form(self, past_user = "", user_error = "", password_error = ""):
        self.response.out.write(form % {"past_username": past_user,
                                        "username": user_error,
                                        "password": password_error})

    def get(self):
        self.write_form()

    def post(self):
        login = self.request.get('username')
        password = self.request.get('password')

        user = User.query(User.username == login, User.password == password)
        user = user.fetch(1)




        if len(user) == 1:
            user = user[0]
            # Create a cookie containing the user id + a hash of ...
            self.response.headers.add_header("Set-Cookie", "user_id=%d" % user.key.id())

            # then redirect
            self.redirect("/welcome")
        else:
            login_err = ""
            pass_err = ""
            if not login:
                login_err = "Please input your login."
            if not pass_err:
                pass_err = "Please input your password"
            if login and pass_err:
                login_err = pass_err = "Please input correct login/password combination."

            self.write_form(login, login_err, pass_err)