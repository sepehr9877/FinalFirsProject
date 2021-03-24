from django.urls import path
from .views import addtodownload,DownloadPage,DeleteFromDownloadPage,link,recentlydownload,MoreDownloadPage,playingdownload
urlpatterns=[
    path("addtodownload/<musicid>",addtodownload),
    path("Downloads",DownloadPage),
    path("DeleteFromDownloadPage/<musicid>",DeleteFromDownloadPage),
    path("media/<MusicFileUrl>",link),
    path("recentlydownload",recentlydownload),
    path("MoreDownloads",MoreDownloadPage),
    path("playsong/id",playingdownload)
]