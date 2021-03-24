import os

from django.db import models
from django.db.models import Q
from django.utils.safestring import mark_safe

from Album.models import Album
from Genre.models import Genre
from Artist.models import Artist
from django.db import connection
from itertools import chain

from download.models import DownloadDetail

cursor=connection.cursor()
import datetime
def getfilename(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext
def upload_image(instance,filename):
    name,ext=getfilename(filename)
    finalname=f"{instance.id}---{instance.title}{ext}"
    return f"music/{finalname}"
def getmusicname(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext
def upload_file(instance,filename):
    name,ext=getmusicname(filename)
    finalname=f"{instance.id}---{instance.title}{ext}"
    return  f"filemusic/{finalname}"
class Music(models.Model):
    title=models.CharField(max_length=150,default="Music")
    release_date=models.CharField(max_length=150)
    length=models.CharField(max_length=150,default="00")
    image=models.ImageField(upload_to=upload_image,null=True,blank=True)
    SongFile=models.FileField(upload_to=upload_file,null=True,blank=True)
    time_add=models.DateTimeField(default=datetime.datetime.now())
    PriceMusic=models.CharField(default=100,max_length=150)
    def __str__(self):
        return self.title
    def get_image(self):
        return mark_safe("<img src='/media/%s',width='50'height='50'>"%self.image)
# Create your models here.
class MusicDetailManager(models.Manager):
    def get_id_by_name(self,albumname):
        albums=MusicDetail.objects.filter(albumdetail__AlbumName=albumname).values_list("musicname_id")
        print("albums")
        print(albums)
        musicid=[]
        for i in albums:
            musicid.append(i[0])
        musicid=list(dict.fromkeys(musicid))
        genre=[]
        music=[]
        for i in musicid:
            genre.extend(MusicDetail.objects.filter(musicname_id=i).values_list("Genredetail_id"))
            if len(genre)>1:
               music.extend(MusicDetail.objects.filter(musicname_id=i,Genredetail_id=genre[0]))
               genre=[]
            else:
                music.extend(MusicDetail.objects.filter(musicname_id=i))
                genre=[]

        print(musicid)
        return music
    def get_artist(self,albumname):
        albums=MusicDetail.objects.select_related("albumdetail").filter(albumdetail__AlbumName=albumname)
        artist=albums.select_related("Artistdetail")
        return artist
    def get_music_by_genre(self,genrename):
        musicsdetail=MusicDetail.objects.filter(Genredetail__NameGenre__contains=genrename)
        music=musicsdetail.select_related("musicname").distinct()

        return music

    def get_artist_by_artistname(self,artisname):
        print("enter")
        musicdetail=MusicDetail.objects.filter(Artistdetail__ArtistName__contains=artisname).values_list("musicname_id").distinct()
        print(musicdetail)
        GenreMusic=[]
        Song_selected=[]
        for i in musicdetail:
            GenreMusic.extend(MusicDetail.objects.filter(musicname_id=i[0]).values_list("Genredetail_id"))
            print("Genre")
            print(GenreMusic)
            if len(GenreMusic)>1:
                print("enter1")
                Song_selected.extend(MusicDetail.objects.filter(musicname_id=i[0],Genredetail_id=GenreMusic[0]))
                print(Song_selected)
                GenreMusic=[]
            else:
                print("else")
                Song_selected.extend(MusicDetail.objects.filter(musicname_id=i[0]))
                print(Song_selected)
                GenreMusic=[]
        return Song_selected
    def get_related_song_by_artist(self,artistname):
        selected_genre=MusicDetail.objects.filter(Artistdetail__ArtistName=artistname).values_list("Genredetail__NameGenre").distinct()
        list_song=[]
        print("selected_genre")
        print(selected_genre)

        for i in selected_genre:
            list_song.extend(MusicDetail.objects.filter(Genredetail__NameGenre__contains=i[0]).values_list("musicname_id"))
        print("listsong")
        list_song=list(dict.fromkeys(list_song))
        music_related=[]
        genre=[]
        for s in list_song:
            genre.extend(MusicDetail.objects.filter(musicname_id=s[0]).values_list("Genredetail_id"))
            if len(genre)>1:
                music_related.extend(MusicDetail.objects.filter(musicname_id=s[0],Genredetail_id=genre[0][0]))
                genre=[]
            else:
                music_related.extend(MusicDetail.objects.filter(musicname_id=s[0]))
        return music_related
    def get_genre_by_artistname(self,artistname):
        print(artistname)
        selected_Song = MusicDetail.objects.filter(Artistdetail__ArtistName=artistname).values_list("Genredetail__NameGenre").distinct()
        print(selected_Song)
        list_moresong = []
        for i in selected_Song:
            list_moresong.extend(MusicDetail.objects.filter(Genredetail__NameGenre__contains=i[0]).values_list("musicname"))
        list_moresong=list(dict.fromkeys(list_moresong))
        Music_list=[]
        for s in list_moresong:
            Music_list.extend(Music.objects.filter(id=s[0]))
        return Music_list
    def SearchSong(self,name):
        print(name)
        lookup=Q(musicname__title__contains=name)|Q(albumdetail__AlbumName__contains=name)|Q(Artistdetail__ArtistName__contains=name)|Q(Genredetail__NameGenre__contains=name)
        SongSearch=MusicDetail.objects.filter(lookup).distinct()
        print(SongSearch)
        return SongSearch
    def get_relatedalbum_by_name(self,name):
        genremusic=MusicDetail.objects.filter(albumdetail__AlbumName=name).values_list("Genredetail_id").distinct()
        albumid=MusicDetail.objects.filter(albumdetail__AlbumName=name).values_list("albumdetail_id")
        print("genre_related_album")
        print(genremusic)
        album_selected=[]
        for i in genremusic:
            album_selected.extend(MusicDetail.objects.filter(Genredetail_id=i[0]).values_list("albumdetail_id"))
        album=[]
        for i in album_selected:
            album.append(i[0])
        album=list(dict.fromkeys(album))
        select_related_album=[]
        genre=[]
        for i in album:
            if i !=albumid[0]:
                genre.extend(MusicDetail.objects.filter(albumdetail_id=i).values_list("Genredetail_id"))
                if len(genre)>1:
                    select_related_album.extend(MusicDetail.objects.filter(albumdetail_id=i,Genredetail_id=genre[0]))
                    genre=[]
                else:
                    select_related_album.extend(MusicDetail.objects.filter(albumdetail_id=i))
        print("select_related_album")
        print(select_related_album)
        print("album_selected")
        print(album_selected)
        musicid=[]

        return select_related_album

class MusicDetail(models.Model):
    musicname=models.ForeignKey(Music,null=True,on_delete=models.PROTECT)
    albumdetail=models.ForeignKey(Album,null=True,on_delete=models.PROTECT)
    Genredetail=models.ForeignKey(Genre,null=True,on_delete=models.PROTECT)
    Artistdetail=models.ForeignKey(Artist,null=True,on_delete=models.PROTECT)
    objects=MusicDetailManager()
    def __str__(self):
        return self.musicname.title

