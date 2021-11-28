# step 7.5: create urls.py file inside app and add urlpatterns, path

from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index')
]