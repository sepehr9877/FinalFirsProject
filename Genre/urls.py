from django.urls import path
from .views import genrepage,GenreSingle,GenreMore
urlpatterns=[
    path("Genre",genrepage),
    path("GenreSingle/<genrename>",GenreSingle),
    path("Genremore/<genrename>",GenreMore)
]