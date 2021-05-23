from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Dojos(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    desc=models.TextField(null=True)
  
class Ninjas(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    dojos_id=models.ForeignKey(Dojos, related_name="ninjas", on_delete = models.CASCADE)