from django.urls import path
from .views import addtofavorit,Favoritpage,DeleteFromFavorit
urlpatterns=[
    path("addtofavorit/<musicid>",addtofavorit),
    path("Favorit",Favoritpage),
    path("deletefavorit/<musicid>",DeleteFromFavorit)
]