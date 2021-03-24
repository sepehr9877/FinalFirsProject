from django.urls import path

from .views import save_visitors_info
urlpatterns=[
    path("Visitors",save_visitors_info)
]