# step 7.4: add index function in view.py file
# step 8.1: In app, views.py import model and add sql quary to list all the book.

from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    all_book = Book.objects.all()
    return render(request,'book_outlet/index.html', {
        'books': all_book
    })