from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField()
    isAvaliable = models.BooleanField(default=True)