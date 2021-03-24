from django.urls import path
from .views import  commentspage,adding_subscriber,allblogspage
urlpatterns=[
    path("commentspage/<blogid>",commentspage),
    path("addingsubscriber/<blogid>",adding_subscriber),
    path("allblogs",allblogspage)
]