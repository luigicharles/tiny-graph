import os
import mongoengine
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.graphql import GraphQLApp
from starlette.config import Config
from api.schema import schema

MONGO_URI = Config(os.path.join('config', '.mongo.env'))('MONGO_URI')

mongoengine.connect("tiny-graph", host=MONGO_URI, alias="default")

routes = [Route('/', GraphQLApp(schema=schema))]

middleware = [
    Middleware(TrustedHostMiddleware, allowed_hosts=['*']),
    Middleware(CORSMiddleware,
               allow_origins=['*'],
               allow_headers=['*'],
               allow_methods=['*'],
               allow_credentials=True)
]

app = Starlette(routes=routes, middleware=middleware)
