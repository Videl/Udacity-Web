from google.appengine.ext import ndb


class User(ndb.Model):
    username = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    salt = ndb.StringProperty(indexed=False)