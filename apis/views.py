from django.shortcuts import render
from rest_framework import generics

from books.models import Books
from .serializer import BookSerializers

# Create your views here.

class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializers