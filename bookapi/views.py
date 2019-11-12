from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerialization

# Create your views here.

class BookOperations(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialization