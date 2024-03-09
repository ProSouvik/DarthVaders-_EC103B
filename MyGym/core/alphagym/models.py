from django.db import models
from django.contrib.auth.models import User

class comment(models.Model):
    user = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class contect(models.Model):
    phone_no = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
