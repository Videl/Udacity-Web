from google.appengine.ext import ndb


class Post(ndb.Model):
    subject = ndb.StringProperty(indexed=True)
    content = ndb.StringProperty(indexed=False)