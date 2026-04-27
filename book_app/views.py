from django.shortcuts import render
from django.views.generic import ListView, DeleteView, View
from .models import Books, Authors
from django.http import HttpResponse

class MyListView(View):
    model = None
    template_name = None
    context_object_name = None

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self, request, *args, **kwards):

        context = {
            self.context_object_name: self.get_queryset()
        }

        return HttpResponse(render(request, self.template_name, context))


class MainPage(MyListView):
    template_name = 'index.html'
    model = Books
    context_object_name = 'books'

    def get_queryset(self):
        return self.model.objects.filter(title__startswith='К')

class AuthorPage(DeleteView):
    template_name = 'author.html'
    model = Authors
    context_object_name = 'author'