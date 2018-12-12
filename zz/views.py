from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.

class BookList(generic.ListView):
    template_name = 'zz/index.html'
    context_object_name = 'booklist'

    def get_queryset(self):
        return Book.objects.all()