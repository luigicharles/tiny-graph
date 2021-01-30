from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    ListField,
    ReferenceField,
    StringField,
)


class User(Document):
    meta = {"collection": "users"}
    username = StringField()
    email = StringField()
    posts = ListField(ReferenceField('Post'))
    friends = ListField(ReferenceField('User'))
    datetime_created = DateTimeField()


class Post(Document):
    meta = {"collection": "posts"}
    title = StringField()
    summary = StringField()
    content = StringField()
    datetime_created = DateTimeField()