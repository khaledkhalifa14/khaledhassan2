"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from PIL import PILLOW_VERSION

# Create your models here.

class UserProfile (models.Model) :
    user = models.OneToOneField(User)
    description= models.CharField(max_length =100,default= '')
    city = models.CharField (max_length = 100,default='')
    website=models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.FileField(null =True,blank=True)
