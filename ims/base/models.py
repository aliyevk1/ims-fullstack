from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)