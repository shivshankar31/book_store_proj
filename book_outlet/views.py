# step 7.4: add index function in view.py file
# step 8.1: In app, views.py import model and add sql quary to list all the book.
# step 9.2: In app/view.py create function and return the value
# step 12.2: convert argument id to slug and compare slug = slug 


from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.urls.conf import include
from .models import Book

# Create your views here.

def index(request):
    all_book = Book.objects.all()
    return render(request,'book_outlet/index.html', {
        'books': all_book
    })

def detail_book(request, slug):
    # try:
    #     book = Book.objects.get(id = id)
    # except: 
    #     raise Http404
    book = get_object_or_404(Book, slug = slug)
    return render(request, 'book_outlet/detail_book.html',{
        'title' : book.title,
        'author' : book.author,
        'rating' : book.rating,
        'is_bestselling': book.is_bestselling 
    }) 