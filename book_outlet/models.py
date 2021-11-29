# step 1.3: In app models.py create class and field which creates DB structure, (Note: uniq identifier with auto increment is not requuired because it will be created automaticly)
# step 4.1: In models.py, define __str__ with f string to view the book entries, to view the entries you have the quit the shell and reload.
# step 4.2: now we have added new fileds author and is bestselling also set validator to rating by importing max and minlenghtvalidator, now run "makemigrations" and new file 0003 will be created. run "migrate" to add in the DB
# step 10.3: In models.py add get_absolute_url function and point url name



from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.urls import reverse 
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MaxLengthValidator(5), MinLengthValidator(1)])
    author = models.CharField(null = True,max_length=50)
    is_bestselling = models.BooleanField(default= False)


    def get_absolute_url(self):
        return reverse("details_book", args=[self.id])
    



    def __str__(self):
        return f'{self.title},({self.rating}), {self.author},{self.is_bestselling}'
