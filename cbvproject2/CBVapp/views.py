from django.shortcuts import render
from django.views.generic import ListView,DetailView
from CBVapp.models import Book

# Create your views here.

class BookListView(ListView):
    model = Book
    #default template: book_list.html ---> you just need to define it with same name in templates
    #template_name = 'CBVapp/books.html' # you can refer to you custom template also
    #default context object: book_list
    #context_object_name ='list_of_books' # you can change it also your custom

class BookDetailView(DetailView):
    model = Book
    #default template: book_detail.html
    #default context: book or object
    # as we change these in ListView we can change to custom name
