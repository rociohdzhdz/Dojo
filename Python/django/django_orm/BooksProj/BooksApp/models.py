from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField(default='')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Publisher(models.Model):
    first_name=models.CharField(max_length=45, default='')
    last_name=models.CharField(max_length=45, default='')
    notes=models.TextField(default='')
    books= models.ManyToManyField(Book, related_name="publishers")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
