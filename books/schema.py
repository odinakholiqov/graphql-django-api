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
    authors = graphene.List(AuthorType)


    def resolve_books(self, info, **kwargs):
        return Book.objects.all()
    
    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()
    

schema = graphene.Schema(query=Query)