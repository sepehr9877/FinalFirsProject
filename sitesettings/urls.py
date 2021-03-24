from django.urls import path
from .views import emailview
urlpatterns=[
    path("sendemail",emailview)
]
