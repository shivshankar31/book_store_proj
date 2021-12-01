# step 15.1: in app admin.py file add "admin.site.register(Book)", which allow us to access in admin panel.
# step 16.1: add BookAdmin class, here (ModelAdmin) you can allow some fields to make read only editable etc. poplated_field used to auto populate 
# step 17.1: list_display added to admin.py which adds fields to display.
# step 17.2 : list_filter added to admin.py which adds filters.
# step 21.1: admin panel asccess to new class "admin.site.register(Author)"
# step 21.2: create class for Author and try adding display and filter

from django.contrib import admin
from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug' : ('title', )}
    list_display = ('title', 'author', 'rating', 'is_bestselling')
    list_filter = ('rating', 'is_bestselling')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)