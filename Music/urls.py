from django.urls import path
from .views import autoplayermusic, SearchMusic, TopSong, LastSong, All_last_song,OfferingSong

urlpatterns=[
    path("artist/<musicfile>",autoplayermusic),
    path("Search",SearchMusic.as_view()),
    path("TopSong",TopSong),
    path("NewReleased",LastSong,name="NewReleased"),
    path("All_last_song",All_last_song),
    path("offeredsong",OfferingSong),

]