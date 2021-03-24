import os

from django.contrib.auth.models import User
from django.db import models
def getfilename(filepath):
    basename=os.path.basename(filepath)
    name,ext=os.path.splitext(basename)
    return name,ext
def upload_user_photo(instance,filename):
    name,ext=getfilename(filename)
    finalname=f"{instance.id}--{instance.user_sub.username}{ext}"
    return f"User/{finalname}"
class UserProfile(models.Model):
    user_sub=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    image_user=models.ImageField(upload_to=upload_user_photo,default="User/104631-200.png")
    def __str__(self):
        return self.user_sub.username
# Create your models here.
