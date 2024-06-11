"""
Schema defines object types
GraphQL represents objects as a graph structure

"""

import graphene
from graphene_django import DjangoObjectType
from .models import Book, Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"

    

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"



class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_books(root, id, **kwargs):
        print("kwargs", kwargs)
        print("id", id)
        print("root", root)
        id = kwargs.get("id", False)

        if id:
            return Book.objectes.get(pk=id)
        
        return Book.objects.all()


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)