import graphene
from api.queries import Query
from api.mutations import Mutations
from api.types import Types

schema = graphene.Schema(
    query=Query,
    mutation=Mutations,
    types=Types)
