from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'author', 'isbn')
    ordering_fields =  ("price", "published_year", "pages")