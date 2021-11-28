# step 7.4: add index function in view.py file

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'book_outlet/index.html')