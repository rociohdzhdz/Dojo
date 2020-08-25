from django.db import models
import datetime
import re

# Create your models here.
class ShowManager(models.Manager):
    def validator(self,postdata):
        errors={}
        if len(postdata['title']) < 2:
            errors['title']= "Title must be more than 2 characters"
        if len(postdata['network']) < 3:
            errors['network']="Network must be more than 3 characters"
        if (postdata['desc']) != '':
            if len(postdata['desc']) < 10:
                errors['desc']="Description is optional but if you add data should be more than 10 characters"
        if (postdata['released']) =='':
            errors['released']="Release Date must have a value"
        return errors
        


class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    releasedate=models.DateField()
    description=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()