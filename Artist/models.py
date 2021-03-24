import os

from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


def getfilename(filepath):
    basename=os.path.basename(filepath)
    name,ext=os.path.splitext(basename)
    return name,ext
def uploadimage(instance,filename):
    name,ext=getfilename(filename)
    finalname=f"{instance.id}---{instance.ArtistName}{ext}"
    return f"Artist/{finalname}"
class Artist(models.Model):
    ArtistName=models.CharField(max_length=150,default="Artist")
    ImageArtsit=models.ImageField(upload_to=uploadimage)

    def __str__(self):
        return self.ArtistName
    def image_tag(self):
        return mark_safe("<img src='/media/%s',width='50'height='50'>"%(self.ImageArtsit))
