from django.urls import path
from .views import HistoryPage,DeleteHistory
urlpatterns=[
    path("History",HistoryPage),
    path("DeleteHistory",DeleteHistory)
]