from django.db import models
import re
# Create your models here.


# Create your models here.
class CourseManager(models.Manager):
    def validator(self,postdata):
        errors={}
        if len(postdata['name']) < 6:
            errors['name']= "Course name must be more than 5 characters"
        if len(postdata['desc']) < 16:
            errors['network']="Description must be more than 15 characters"
        return errors

class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=CourseManager()
