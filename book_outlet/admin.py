# step 15.1: in app admin.py file add "admin.site.register(Book)", which allow us to access in admin panel.
# step 16.1: add BookAdmin class, here (ModelAdmin) you can allow some fields to make read only editable etc. poplated_field used to auto populate 
# step 17.1: list_display added to admin.py which adds fields to display.
# step 17.2 : list_filter added to admin.py which adds filters.

from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug' : ('title', )}
    list_display = ('title', 'author', 'rating', 'is_bestselling')
    list_filter = ('rating', 'is_bestselling')


admin.site.register(Book, BookAdmin)