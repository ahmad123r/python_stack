from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 5:
            errors["fname"] = "The password should be at least 5 characters"
        if len(postData['password']) < 8:
            errors["password"] = "The password  should be at least 8 characters"
        return errors




class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    password1=models.CharField(null=True,max_length=255)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    objects=BlogManager()

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    upload_by=models.ForeignKey(User,related_name="books",on_delete=CASCADE)
    liked_by=models.ManyToManyField(User,related_name="liked_books")
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
