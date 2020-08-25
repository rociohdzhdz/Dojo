from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validator(self,postdata):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
        if len(postdata['fname'])<2:
            errors['fname']= "Your name must be more than 2 chars"
        if len(postdata['lname'])<2:
            errors['lname']="Your last name must be more than 2 chars"
        if not EMAIL_REGEX.match(postdata['mail']):
            errors['mail']="Email must be a valid format"
        if len(postdata['password'])<8:
            errors['password']="Password must be at least 8 characters"
        if postdata['password'] != postdata['confirmpass']:
            errors['confirmpass']="Your password and confirm password should match"
        return errors


class QuoteManager(models.Manager):
    def validator(self,postdata):
        errors={}
        if len(postdata['author'])<3:
            errors['author']="Author must be at least 3 chars"
        if len(postdata['quotedes'])<10:
            errors['quotedes']="Your quote must be at least 10 chars"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


class Quote(models.Model):
    author=models.CharField(max_length=255)
    quotedes=models.TextField()
    poster=models.ForeignKey(User,related_name="quotes", on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name="likes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=QuoteManager()