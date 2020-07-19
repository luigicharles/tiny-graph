import graphene
import graphene_federation

from gql.queries   import Query       as GrapheneQueries
from gql.mutations import Mutations   as GrapheneMutations

from mongo.objects import Note, User

schema = graphene_federation.build_schema(query    = GrapheneQueries,
                                          mutation = GrapheneMutations,
                                          types    = [Note,User])