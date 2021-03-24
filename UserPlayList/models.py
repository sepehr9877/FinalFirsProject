import os

from django.contrib.auth.models import User
from django.db import models
def get_filepath(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext
def upload_song_user(instance,filename):
    name,ext=get_filepath(filename)
    finalname=f"{instance.id}---{instance.SongName}{ext}"
    return f"Usersong/{finalname}"
def upload_image_playlist(instance,filename):
    name,ext=get_filepath(filename)
    finalnam=f"{instance.id}--{instance.PlayListName}{ext}"
    return f"Playlistimage/{finalnam}"
class MusicFile(models.Model):
    SongFile = models.FileField(upload_to=upload_song_user, null=True, blank=True)
    SongName = models.CharField(max_length=150,null=True)
    ArtistName = models.CharField(max_length=150,null=True)
    AlbumName = models.CharField(max_length=150,null=True)
    is_paid=models.BooleanField(default=False)
    is_favorit=models.BooleanField(default=False)
    def __str__(self):
        return self.SongName
class Add_PlayList(models.Model):
    PlayListName=models.CharField(max_length=150,default="Name")
    PlayListImage=models.ImageField(upload_to=upload_image_playlist,null=True,blank=True)
    Status=models.BooleanField(default=True)
    def __str__(self):
        return self.PlayListName
class PlayListDetailManager(models.Manager):
    def get_playlist_byname(self,playlistname,userid):
        selected_playlist=PlayListDetail.objects.filter(UserPlayList_id=userid,PlayListSelect__PlayListName__contains=playlistname)
        print("enter")
        print(selected_playlist)
        return selected_playlist

class PlayListDetail(models.Model):
    UserPlayList=models.ForeignKey(User,on_delete=models.PROTECT)
    PlayListSelect=models.ForeignKey(Add_PlayList,on_delete=models.CASCADE)
    Music_File = models.ForeignKey(MusicFile, null=True, on_delete=models.PROTECT)
    objects=PlayListDetailManager()
    def __str__(self):
        return self.UserPlayList.username + self.PlayListSelect.PlayListName

# Create your models here.
