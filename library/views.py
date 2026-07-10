from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination



# Create your views here.
class BookPagination(PageNumberPagination):
    page_size = 5


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

        filter_backends = (
            filters.SearchFilter,
            filters.OrderingFilter,
            DjangoFilterBackend,
        )

        search_fields = (
            "title",
            "author",
            "isbn",
        )

        ordering_fields = (
            "price",
            "published_year",
            "pages",
        )

        filterset_fields = (
            "is_available",
            "published_year",
        )

