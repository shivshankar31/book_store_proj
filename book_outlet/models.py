# step 1.3: In app models.py create class and field which creates DB structure, (Note: uniq identifier with auto increment is not requuired because it will be created automaticly)
# step 4.1: In models.py, define __str__ with f string to view the book entries, to view the entries you have the quit the shell and reload.
# step 4.2: now we have added new fileds author and is bestselling also set validator to rating by importing max and minvaluvalidator, now run "makemigrations" and new file 0003 will be created. run "migrate" to add in the DB
# step 10.3: In models.py add get_absolute_url function and point url name
# step 11.1: add slug field to the class Book in modules.py
# step 11.2: modify default save module, add Super().save() in order to recall the orginal save method.
# step 11.3: open shell "python3 manage.py shell" and run below get() and call save()
# step 12.3: change get_absolute_url function args to self.slug
# step 12.4: add "db_index = True" to the slug field, it will increases the performance. index can be used where you use it more just to increase the performance.
# step 15.3: In models.py, slug feild pass blank = True amd editable = False and check
# step 16.2: now the save redefine can be removed because it is populated at admin.py file.
# step 18.1: add Author class with first name and last name feild in models.py.
# step 18.2: replace author field in Book class using "model.foreignkey(Author, on-delete= CASCADE, null=true". 
# step 18.3: run makemigrations and migrate the changes (delete all old records, because it will show some error as we change the schema)
# step 20.3: related_name , where we can specify our own name for model.forignkey. In models.py add related__name
# step 21.3: redefine __str__function using f' ' string in order to display the object in admin panel
# step 21.4: we can also create a templet function as fullname so that we can use it some other place as well 
# step 22.1: create Address class with stree, postcode, location and country in models.py file
# step 22.6: add nested Meta class to display Address correctly in admin panel. django will always take the model name and add 's' at the end in models.py


from django.contrib.admin.decorators import display
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.urls import reverse 
from django.utils.text import slugify
# Create your models here.

class Address(models.Model):
    stree = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Address Master"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address,on_delete=models.CASCADE, null=True)
    # method 1:step 21.3
    #def __str__(self):
    #    return f'{self.first_name} {self.last_name}'

    # method 2 : step 21.4
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullname()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[ MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name= 'xyz')
    is_bestselling = models.BooleanField(default= False)
    slug = models.SlugField(default="", blank = True, null= False, db_index=True)

    def get_absolute_url(self):
        return reverse("details_book", args=[self.slug])

    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, *kwargs)
    
    def __str__(self):
        return f'{self.title},({self.rating}), {self.author},{self.is_bestselling}'
