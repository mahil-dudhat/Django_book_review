from re import M
from statistics import mode
from django.db import models

# Create your models here.

class public_book_data(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=50)
    book_image = models.TextField(max_length=50)
    book_author = models.TextField()

    class Meta:
      db_table="public_book_data"