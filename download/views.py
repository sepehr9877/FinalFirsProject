from django.shortcuts import render, redirect
from .models import DownloadDetail,DownloadSong
from Artist.models import Artist
from Music.models import Music,MusicDetail
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import urllib
import datetime
import requests
def addtodownload(request,*args,**kwargs):
    musicid=kwargs["musicid"]
    Selected_Artistname=Artist.objects.filter(musicdetail__musicname_id=musicid).first()
    userid=request.user.id
    DownloadUser=DownloadDetail.objects.check_id(userid)
    downloaddetail=DownloadDetail.objects.filter(Download_id=DownloadUser.id,MusicDownload_id=musicid).first()
    if downloaddetail is None:
        addmusic=DownloadDetail.objects.create(Download_id=DownloadUser.id,MusicDownload_id=musicid)
    return redirect("/Downloads")
def DownloadPage(request,*args,**kwargs):
    userid=request.user.id
    DownloadDetails=DownloadDetail.objects.filter(Download__UserDownload_id=userid)
    musicid=DownloadDetails.values_list("MusicDownload_id")
    print(musicid)
    GetmusicDetail=[]
    selected_song=[]
    for i in musicid:
        selected_song.extend(MusicDetail.objects.filter(musicname_id=i[0]).values_list("Genredetail_id"))
        if len(selected_song)>1:
            selected_song=selected_song[0][0]
            GetmusicDetail.extend(MusicDetail.objects.filter(musicname_id=i[0],Genredetail_id=selected_song))
            selected_song=[]
        else:
            GetmusicDetail.extend(MusicDetail.objects.filter(musicname_id=i[0]))
    context={"GetmusicDEtail":GetmusicDetail
             }
    return render(request,"DownloadPage.html",context)
def DeleteFromDownloadPage(request,*args,**kwargs):
    userid=request.user.id
    musicid=kwargs["musicid"]
    Selected_download_delete=DownloadDetail.objects.filter(Download__UserDownload_id=userid,MusicDownload_id=musicid).delete()
    return redirect("/Downloads")
# Create your views here.
def link(request,*args,**kwargs):
    MusicFile=kwargs["MusicFileUrl"]
    print("enter")
    listmusicid=Music.objects.filter(SongFile=MusicFile).first()
    userid=request.user.id
    print("user download id")
    print(userid)
    Downloaduser=DownloadSong.objects.filter(UserDownload_id=userid).first()
    print("updated_recently_download")
    updated_recently_download = DownloadDetail.objects.update_or_create(Download_id=Downloaduser.id,MusicDownload_id=listmusicid.id,recnetlydownload=datetime.datetime.now())
    print("hello")
    return redirect(f"/media/{MusicFile}")



def recentlydownload(request):
    userid=request.user.id
    recently_downloaded=DownloadDetail.objects.filter(Download__UserDownload_id=userid).order_by('-recnetlydownload')[:4]
    context={"rencently_download":recently_downloaded}
    return render(request,"rencentlydownloaded.html",context)
def MoreDownloadPage(request):
    userid=request.user.id
    AllDownloads=DownloadDetail.objects.filter(Download__UserDownload_id=userid)
    context={"AllDownloads":AllDownloads}
    return render(request,"MoreDownload.html",context)
def DownloadListUser(request):
    userid=request.user.id
    DownloadUser=DownloadDetail.objects.Get_User_Download(userid)
    context={"DownloadUser":DownloadUser}
    print(DownloadUser)
    return render(request,"AutoPlayer.html",context)
def playingdownload(request,*args,**kwargs):
    musicid=kwargs["id"]
    selected_music=MusicDetail.objects.filter(id=musicid).first()
    context={"selected_music":selected_music}
    return render(request,"AutoPlayer.html",context)
