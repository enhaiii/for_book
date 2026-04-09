from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView
from .models import *

class MainPage(ListView):
    template_name = 'index.html'
    model = Books
    context_object_name = 'books'

class AuthorPage(DeleteView):
    template_name = 'author.html'
    model = Authors
    context_object_name = 'authors'