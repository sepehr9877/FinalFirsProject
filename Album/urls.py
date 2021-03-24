import os

from django.urls import path
from .views import AlbumPage,AlbumSinglePage,AllSongs,ViewMoreSong,allalbums
urlpatterns=[
    path("Albums",AlbumPage),
    path("Albums/<AlbumName>",AlbumSinglePage),
    path("AllSongs",AllSongs),
    path("allrelatedalbumsong/<albumname>",ViewMoreSong ),
    path("allalbums",allalbums)
]