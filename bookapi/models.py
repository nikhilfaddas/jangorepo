from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    publication = models.CharField(max_length=100)
    reviews = models.CharField(max_length=100)
