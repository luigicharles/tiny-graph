import graphene

from mongo.objects import Note as NoteObject

from mongo.models import Note as NoteModel

class CreateNote(graphene.Mutation):
    '''
        Creates a Note, given some inputs, this is 
        the inputs that the user supplies in fields from 
        the frontend.
    '''
    class Arguments:

        title = graphene.String()
        username = graphene.String()
        summary = graphene.String()
        content = graphene.String()

    ok = graphene.Boolean()
    note = graphene.Field(lambda: NoteObject)

    def mutate(root, info,title,username,summary,content):
        # Instantiate a new note model.
        note  = NoteModel(
            title     = title,
            summary   = summary,
            content   = content)
        # Saves note
        note.save()
        # Gets author user model.
        author  = list(UserModel.objects(username=username))[0]
        # Adds note to user model and save.
        author.notes.append(note); author.save()
        # Returns ok status.
        ok = True
        return CreateNote(note=note,ok=ok)

class C_Mutations(graphene.ObjectType):

    create_note   = CreateNote.Field()



