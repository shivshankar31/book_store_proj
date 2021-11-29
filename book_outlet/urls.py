# step 7.5: create urls.py file inside app and add urlpatterns, path
# step 9.2: In urls.py assign the path for the new function


from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<id>', views.detail_book)
]