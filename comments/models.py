import os

from django.contrib.auth.models import User
from django.db import models
import datetime

from django.utils.safestring import mark_safe


def getfilename(filepath):
    filename=os.path.basename(filepath)
    name,ext=os.path.splitext(filename)
    return name,ext
def uploadimage(instance,filename):
    name,ext=getfilename(filename)
    finalename=f"{instance.id}--{instance.username}{ext}"
    return f"user/{finalename}"
def get_blog_filename(filepath):
    filename=os.path.basename(filepath)
    name,ext=os.path.splitext(filename)
    return name,ext
def upload_image_blog(instance,filename):
    name,ext=get_blog_filename(filename)
    finalname=f"{instance.id}---{instance.title}{ext}"
    return f"blog/{finalname}"
class Blogs(models.Model):
    title=models.CharField(max_length=150)
    descriptionblog=models.TextField(max_length=1000)
    image=models.ImageField(upload_to=upload_image_blog,null=True)
    time=models.DateTimeField(default=datetime.datetime.now())
class Comments(models.Model):
    time_comments=models.DateTimeField(default=datetime.datetime.now())
    descriptions=models.TextField(max_length=500)
    # def __str__(self):
    #     return f"{self.time_comments}"
class Subscriber(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    image=models.ImageField(upload_to=uploadimage,null=True,blank=True)
    def __str__(self):
        return self.username
    def image_tag(self):
        return mark_safe("<img src='/media/%s',width='50' height='50'>"%(self.image))
class User_Comments(models.Model):
    user_comment=models.ForeignKey("Subscriber",on_delete=models.PROTECT)
    comments=models.ForeignKey('Comments',on_delete=models.CASCADE)
    blog_comments=models.ForeignKey('Blogs',on_delete=models.PROTECT,null=True)
    # def __str__(self):
    #     return self.user_comment
    def get_time_of_comment(self):
        return self.comments.time_comments
    def get_image_user(self):
        return self.user_comment.image_tag()
# Create your models here.
