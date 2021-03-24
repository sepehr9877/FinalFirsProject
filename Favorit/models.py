from django.contrib.auth.models import User
from django.db import models
from Music.models import Music,MusicDetail
import datetime

# from download.models import DownloadDetail
from download.models import DownloadDetail


class FavoritDetailManger(models.Manager):
    def check_id(self,userid):
        selected_user=FavoritMusic.objects.filter(FavoritUser_id=userid).first()
        if selected_user is None:
            selected_user=FavoritMusic.objects.create(FavoritUser_id=userid)
            return selected_user
        return selected_user
    def get_favorit_user_song(self,userid):
        listsong=[]
        print("startlistsong")
        print(listsong)
        selected_song=FavoritDetail.objects.filter(DetailFavortiUser__FavoritUser_id=userid).distinct().values_list("FavoritSong_id")
        for i in selected_song:
            listsong.append(i[0])
        print("resaultlistsong")
        print(listsong)
        return listsong
    def get_offered_song_user(self,userid):
        Favorit_user_Song = FavoritDetail.objects.filter(DetailFavortiUser__FavoritUser_id=userid).values_list(
            "FavoritSong_id")
        Download_user_Song = DownloadDetail.objects.filter(Download__UserDownload_id=userid).values_list(
            "MusicDownload_id")
        if not Favorit_user_Song or not Download_user_Song:
            final_music=list(MusicDetail.objects.all())
            print("hello")
        else:
            selected_list_music = []
            for i in Favorit_user_Song:
                selected_list_music.append(i[0])
            for j in Download_user_Song:
                selected_list_music.append(j[0])
            selected_list_music = list(dict.fromkeys(selected_list_music))
            selected_genre = []
            for s in selected_list_music:
                selected_genre.extend(MusicDetail.objects.filter(musicname_id=s).values_list("Genredetail_id"))
            selected_song = []
            for g in selected_genre:
                selected_song.extend(MusicDetail.objects.filter(Genredetail_id=g[0]).distinct())

            favorit_download_song_user = []
            for m in selected_list_music:
                favorit_download_song_user.extend(MusicDetail.objects.filter(musicname_id=m).distinct())
            final_music = []
            print(selected_song)
            print(favorit_download_song_user)
            final_music = list(set(selected_song) ^ set(favorit_download_song_user))
            print(final_music)
        return final_music

class FavoritMusic(models.Model):
    FavoritUser=models.ForeignKey(User,on_delete=models.PROTECT)
    TimeFavorti=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.FavoritUser.username
class FavoritDetail(models.Model):
    DetailFavortiUser=models.ForeignKey(FavoritMusic,on_delete=models.PROTECT)
    FavoritSong=models.ForeignKey(Music,on_delete=models.PROTECT)
    objects=FavoritDetailManger()
    def __str__(self):
        return  self.DetailFavortiUser.FavoritUser.username + self.FavoritSong.title



# Create your models here.
