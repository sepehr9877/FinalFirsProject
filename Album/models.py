import os

from django.utils.safestring import mark_safe

from Artist.models import Artist
from django.db import models
def getfilename(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext
def upload_image(instance,filename):
    name, ext = getfilename(filename)
    finalname = f"{instance.id}--{instance.AlbumName}{ext}"
    return f"Album/{finalname}"
class AlbumManager(models.Manager):
    def get_relatedalbum_by_name(self,name):
       pass
class Album(models.Model):
    Year=models.CharField(max_length=150,default="2000")
    AlbumName=models.CharField(max_length=150,default="unknown")
    AlbumImage=models.ImageField(upload_to=upload_image)
    objects=AlbumManager()
    def __str__(self):
        return self.AlbumName
    def image_tag(self):
        return mark_safe('<img src="/media/%s",width="50" height="50"/>' %(self.AlbumImage))

# Create your models here.
