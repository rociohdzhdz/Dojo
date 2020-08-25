from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validator(self,postdata):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['fname'])<2:
            errors['fname']="Your name must be more than 2 chars"
        if len(postdata['lname'])<2:
            errors['lname']="Your last name must be more than 2 chars"
        if not EMAIL_REGEX.match(postdata['mail']):
            errors['mail']="Email must be valid format"
        if len(postdata['pass'])<8:
            errors['pass']="Password must be at least 8 chars"
        if postdata['pass'] != postdata['cpass']:
            errors['cpass']="Password and confirm password must be the same"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class MessageManager(models.Manager):
    def validator(self, form):
        errors={}
        if len(form['content'])<5:
            errors['length']="Message must be at least 5 characters"
        return errors


class wallMessage(models.Model):
    content=models.CharField(max_length=255)
    poster=models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=MessageManager()

class Comment(models.Model):
    content=models.CharField(max_length=255)
    poster=models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE)
    message=models.ForeignKey(wallMessage, related_name="comments", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)