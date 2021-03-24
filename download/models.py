from django.contrib.auth.models import User
from django.db import models

import datetime
from Album.models import Album

# Create your models here.
class DownloadDetailManger(models.Manager):
    def check_id(self,userid):
        userdownload=DownloadSong.objects.filter(UserDownload_id=userid).first()
        if userdownload is None:
            userdownload=DownloadSong.objects.create(UserDownload_id=userid,is_paid=True,Download_Time=datetime.datetime.now())
        return userdownload
    def get_selected_album(self,userid,musicid):
        album_id_selected=DownloadDetail.objects.filter(Download__UserDownload_id=userid).values_list("MusicDownload__musicdetail__albumdetail","MusicDownload_id").distinct()
        album_selected=[]

        print(album_selected)
        return album_selected
    def Get_User_Download(self,userid):
        Selected_Downlod=DownloadDetail.objects.filter(Download__UserDownload_id=userid)
        return Selected_Downlod
    def get_list_songdownload_user(self,userid):
        songid=self.get_queryset().filter(Download__UserDownload_id=userid).values_list("MusicDownload_id")
        print("songid")
        print(songid)
        musicid=[]
        for i in songid:
            musicid.append(i[0])
        print("musicid")
        print(musicid)
        return musicid
    def get_top_artist(self):
        alluser=DownloadSong.objects.all().values_list("UserDownload_id")
        userid=[]
        for i in alluser:
            userid.append(i[0])
        print(userid)
        selectuser=DownloadDetail.objects.filter(Download__UserDownload_id=userid[0]).values_list("MusicDownload_id")
        print(selectuser)
        selectmusic=[]
        variable_song=[]
        help_variable=[]
        for i in selectuser:
            selectmusic.append(i[0])
        print(selectmusic)
        for i in selectmusic:
            for j in range(1,len(userid)):
                add_user=DownloadDetail.objects.get_list_songdownload_user(userid[j])
                print(add_user)
                print(variable_song)
                if not variable_song:
                    for n in add_user:
                        if n==i:
                            variable_song.append(n)
                else:
                    for v in variable_song:
                        for m in add_user:
                            if m==v:
                                help_variable.append(m)
                    print(help_variable)
                    variable_song=[]
                    for h in help_variable:
                        variable_song.append(h)
                    help_variable=[]
        variable_song=list(dict.fromkeys(variable_song))
        print(variable_song)
        if len(variable_song)<3:
            variable_song=[]
            variablesong=DownloadDetail.objects.all().values_list("MusicDownload_id")[:6]
            for i in variablesong:
                variable_song.append(i[0])
            variable_song=list(dict.fromkeys(variable_song))
            return variable_song
        else:
            return variable_song




class DownloadSong(models.Model):
    UserDownload=models.ForeignKey(User,on_delete=models.PROTECT)
    is_paid=models.BooleanField(default=True)
    Download_Time=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return f"{self.UserDownload}"

    def get__time(self):
        return f"{self.Download_Time}"
class DownloadDetail(models.Model):
    Download=models.ForeignKey(DownloadSong,on_delete=models.CASCADE)
    MusicDownload=models.ForeignKey('Music.Music',on_delete=models.PROTECT)
    PriceDownload=models.CharField(max_length=150,default=100)
    recnetlydownload=models.DateTimeField(default=datetime.datetime.now())
    objects=DownloadDetailManger()
    def __str__(self):
        return self.Download.UserDownload.username + self.MusicDownload.title
    def get_image_download(self):
        return self.MusicDownload.get_image()
    def get_user_name(self):
        return self.Download.UserDownload.username
    def get_time(self):
        return f"{self.recnetlydownload}"