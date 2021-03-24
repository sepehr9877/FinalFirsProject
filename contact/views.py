from django.shortcuts import render, redirect
from UserPlayList.models import PlayListDetail
from .models import Followers
from account.models import UserProfile
# Create your views here.
def request_to_user(request,*args,**kwargs):
    palylistid=kwargs["playlistid"]
    userid=request.user.id
    select_user_from=PlayListDetail.objects.filter(PlayListSelect_id=palylistid).values_list("UserPlayList_id")
    print("my")
    print(select_user_from)
    user_to_id=[]
    for i in select_user_from:
        user_to_id.append(i[0])
    send_request_to_user=Followers.objects.update_or_create(from_user_id=userid,to_user_id=user_to_id[0],accept_by_user=False)

    return redirect("/Playlist")
