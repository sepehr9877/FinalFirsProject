from django.urls import path
from .views import request_to_user
urlpatterns=[
    path("Subscribe_touser/<playlistid>",request_to_user)
]