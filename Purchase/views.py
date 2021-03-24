from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Album.models import Album
from Music.models import MusicDetail
from .models import PurchaseUserMusic,PurchaseUser
# Create your views here.
@login_required(login_url="/login")
def CheckPurchase(request,*args,**kwargs):
    userid=request.user.id
    musicid=kwargs["musicid"]
    check_purchase_user:PurchaseUser=PurchaseUserMusic.objects.checkid(userid)
    addtopurchase:PurchaseUserMusic=PurchaseUserMusic.objects.filter(Purchase_User_id=check_purchase_user.id,Music_Purchase_id=musicid)
    if not addtopurchase:
        addtopurchase=PurchaseUserMusic.objects.create(Purchase_User_id=check_purchase_user.id,Music_Purchase_id=musicid)
        return redirect("/purchase")
    return redirect("/purchase")
@login_required(login_url="/login")
def purchasepage(request):
    userid=request.user.id
    username=User.objects.filter(id=userid).values_list("username")
    print("username")
    print(username)
    user=PurchaseUser.objects.filter(user_purchase_id=userid)
    print("user")
    print(user)
    user_purchase=PurchaseUserMusic.objects.filter(Purchase_User__user_purchase_id=userid)
    print(user_purchase)
    context={"user_purchase":user_purchase}
    return render(request,"PurchasePage.html",context)
def delete_frompurchasepage(request,*args,**kwargs):
    userid=request.user.id
    musicid=kwargs["musicid"]
    selected_song=PurchaseUserMusic.objects.filter(Purchase_User__user_purchase_id=userid,Music_Purchase_id=musicid).delete()
    return redirect("/purchase")
def PurchaseFinished(request):
    userid=request.user.id
    # selected_user_purchase=PurchaseUser.objects.filter(user_purchase_id=userid).update(,is_paid=True)
    print("selected_user_purchase")
    # print(selected_user_purchase)
    selectuser=PurchaseUser.objects.filter(user_purchase_id=userid).first()
    isTreuPurchase=PurchaseUserMusic.objects.filter(Purchase_User_id=selectuser.id).update(is_paid_music=True)
    return redirect("/purchase")
@login_required(login_url="/login")
def PurchaseAlbum(request,*args,**kwargs):
    albumname=kwargs["albumname"]
    userid=request.user.id
    selected_music=MusicDetail.objects.filter(albumdetail__AlbumName=albumname).select_related()
    print("selected_muisc")
    check_purchase_user: PurchaseUser = PurchaseUserMusic.objects.checkid(userid)
    for m in selected_music:
        selected_purchase=PurchaseUserMusic.objects.filter(Purchase_User__user_purchase_id=userid,Music_Purchase_id=m.musicname.id)
        if not selected_purchase:
            PurchaseUserMusic.objects.create(Purchase_User_id=check_purchase_user.id,Music_Purchase_id=m.musicname.id)
    return redirect("/purchase")
def TopPurchase(request):
    selected_songs=PurchaseUserMusic.objects.get_common_purchase()
    context={"topodersongs":selected_songs}
    return render(request,"Top_Purchase.html",context)
