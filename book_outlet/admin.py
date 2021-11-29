# step 15.1: in app admin.py file add "admin.site.register(Book)", which allow us to access in admin panel.

from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.register(Book)