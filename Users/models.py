from django.db import models

from django.contrib.auth.models import *
from django.contrib.auth.models import User


class usersmodel(models.Model):

    username = models.CharField(max_length=64)
    usermail = models.EmailField(max_length=254)

    userpassword1 = models.CharField(max_length=254)
    userpassword2 = models.CharField(max_length=254)

    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.username

class blogmodel(models.Model):

    blogname = models.CharField(max_length=20)
    blogname2 = models.CharField(max_length=20)

    def __str__(self):
        return self.blogname