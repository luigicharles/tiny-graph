import graphene
from db.models import User as UserModel
from db.models import Post as PostModel
from db.objects import User as UserObject
from db.objects import Post as PostObject


class Query(graphene.ObjectType):

    user = graphene.List(UserObject, username=graphene.String())
    users = graphene.List(UserObject)

    post = graphene.List(PostObject, title=graphene.String())
    posts = graphene.List(PostObject)

    @staticmethod
    def resolve_user(root, info, username):
        return list(UserModel.objects(username=username))

    @staticmethod
    def resolve_post(root, info, title):
        return list(PostModel.objects(title=title))

    @staticmethod
    def resolve_users(self, info):
        return list(UserModel.objects.all())

    @staticmethod
    def resolve_posts(self, info):
        return list(PostModel.objects.all())
