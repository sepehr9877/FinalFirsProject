from django.urls import path

from account.views import MyRequests, MyFollowers, MyFollowing, MyFriendsPage, accept_my_request, restric_my_follwers, \
    Follow_the_user, MyWaitings,deny_request,UnFollowUsers

urlpatterns=[
    path("MyFreindsPage",MyFriendsPage),
    path("Myfriends",MyRequests,name="MyRequests"),
    path("MyFollowers",MyFollowers,name="MyFollowers"),
    path("MyFollowing",MyFollowing,name="MyFollowing"),
    path("MyWaitings",MyWaitings,name="MyWaitings"),
    path("accept_requests/<from_user>",accept_my_request),
    path("restrict_myfolowers/<from_user>",restric_my_follwers),
    path("Follow_user/<from_user>",Follow_the_user),
    path("deny_request/<to_user>",deny_request),
    path("UnFollow/<to_user>",UnFollowUsers)
]