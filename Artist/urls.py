import os

from django.urls import path
from .views import artistspage,artistsingle,MoreSingleSongArtist,select_for_artistpage,allartistpage
urlpatterns=[
    path("artists",artistspage),
    path("Singleartist/<musicid>",select_for_artistpage),
    path("artist/<artistname>",artistsingle),
    path("morerelatedsong/<artistname>",MoreSingleSongArtist),
    path("AllArtists",allartistpage)
]