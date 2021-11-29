# step 7.5: create urls.py file inside app and add urlpatterns, path
# step 9.2: In urls.py assign the path for the new function
# step 10.1: in urls.py add name to detail_book and also add id as int.
# step 12.1: convert url path to slug:slug


from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<slug:slug>', views.detail_book, name="details_book")
]