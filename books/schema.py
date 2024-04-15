import graphene
from graphene_django import DjangoObjectType
from .models import Book, Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()
    


schema = graphene.Schema(query=Query)