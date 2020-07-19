
import graphene

from mongo.objects import Note as NoteObject 

from mongo.models import Note  as NoteModel

class Query(graphene.ObjectType):

    # Ex: Bulk model queries
    #    Theses queries return all models of a given type 
    #    stored in our mongo atlas cluster. 
    #
    notes    = graphene.List(NoteObject)

    # Ex: Unique key queries
    #   Notes queries take in a unique key of a particular object
    #   and returns a single graphene object of that type.
    #
    note  = graphene.List(NoteObject,title=graphene.String())

    def resolve_notes(self, info):
        # Returns all note models
    	return list(NoteModel.objects.all())

    def resolve_note(root,info,title):
        # Takes in a note title, returns a single note.
        return list(NoteModel.objects(title=title))

