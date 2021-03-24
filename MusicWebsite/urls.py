"""MusicWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import settings, static
from .views import homepage,MainWrapperStart,footerwrapper
from account.views import newregisterinpage,newloginpage,profiledetail,logoutdetail
from Artist.views import artistspage
from Music.views import autoplayermusic
from download.views import recentlydownload,DownloadListUser,playingdownload
urlpatterns = [
    path('sepehradmin/', admin.site.urls),
    path('',homepage),
    path('autoplayermusic', autoplayermusic, name="autoplayermusic"),
    path('recentlydownloaded',recentlydownload,name="recentlydownloaded"),
    path('MainWrapperStart',MainWrapperStart,name="MainWrapperStart"),
    path('profiledetail',profiledetail,name="profiledetail"),
    path('logoutuser',logoutdetail),
    path('Autoplayer',DownloadListUser,name="Autoplayer"),
    path('footerwrapper',footerwrapper,name="footerwrapper"),
    path('',include('account.urls')),
    path('login',newloginpage),
    path('adduser',newregisterinpage),
    path('',include("Album.urls")),
    path('',include("Artist.urls")),
    path('',include("Genre.urls")),
    path('',include("Music.urls")),
    path('',include("download.urls")),
    path('',include("Favorit.urls")),
    path('',include("UserPlayList.urls")),
    path('',include("History_user.urls")),
    path('',include("comments.urls")),
    path('',include("Visitors.urls")),
    path('',include("sitesettings.urls")),
    path('',include("Purchase.urls")),
    path('',include('contact.urls'))
]
if settings.DEBUG:
    urlpatterns=urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)