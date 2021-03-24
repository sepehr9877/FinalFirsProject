import os

from django.db import models
def getfilename(filepath):
    base_name=os.path.basename(filepath)
    name,ex=os.path.splitext(base_name)
    return name,ex
def upload_image(instance,filename):
    name,ex=getfilename(filename)
    finalname=f"{instance.id}----{instance.NameGenre}{ex}"
    return f"Genre/{finalname}"
class Genre(models.Model):
    NameGenre=models.CharField(max_length=150,default="Genre")
    image=models.ImageField(upload_to=upload_image,null=True)
    def __str__(self):
        return self.NameGenre

# Create your models here.
