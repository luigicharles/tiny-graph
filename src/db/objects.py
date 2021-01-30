from graphene_mongo import MongoengineObjectType
from db.models import User as UserModel
from db.models import Post as PostModel


class User(MongoengineObjectType):
    class Meta:
        model = UserModel


class Post(MongoengineObjectType):
    class Meta:
        model = PostModel
