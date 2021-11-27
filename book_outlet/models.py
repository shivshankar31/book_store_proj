# In app models.py create class and field which creates DB structure, (Note: uniq identifier with auto increment is not requuired because it will be created automaticly)

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField