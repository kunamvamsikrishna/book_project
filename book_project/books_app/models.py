from django.db import models

class Book(models.Model):
    title  = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pages = models.IntegerField()
