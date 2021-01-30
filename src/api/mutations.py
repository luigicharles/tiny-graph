import datetime 
import graphene
from db.models import User as UserModel
from db.models import Post as PostModel
from db.objects import User as UserObject
from db.objects import Post as PostObject


class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserObject)

    def mutate(root, info, username, email):
        ok, user = False, None
        if len(list(UserModel.objects(username=username)))\
        + len(list(UserModel.objects(email=email))) == 0:
            user = UserModel(
                username=username,
                email=email,
                posts=[],
                friends=[],
                datetime_created=datetime.datetime.now())
            user.save()
            ok = True
        return CreateUser(user=user, ok=ok)

class CreatePost(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        username = graphene.String()
        summary = graphene.String()
        content = graphene.String()

    ok = graphene.Boolean()
    post = graphene.Field(lambda: PostObject)

    def mutate(root, info, title, username, summary, content):
        ok, post = False, None
        authors = list(UserModel.objects(username=username))
        if len(authors) == 1:
            author = authors.pop()
            post = PostModel(
                title=title,
                summary=summary,
                content=content,
                datetime_created=datetime.datetime.now())
            post.save()
            author.posts.append(post)
            author.save()
            ok = True
        return CreatePost(post=post, ok=ok)


class RemovePost(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        username = graphene.String()

    ok = graphene.Boolean()

    def mutate(root, info, title, username):
        ok, post = False, None
        users = list(UserModel.objects(username=username))
        if len(users) == 1:
            user = users.pop()
            if title in [post.title for post in user.posts]:
                post = [post for post in user.posts if post.title == title]
                post.remove()
                ok = True
        return RemovePost(post=post, ok=ok)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    remove_post = RemovePost.Field()
