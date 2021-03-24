from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import FavoritMusic,FavoritDetail
from Music.models import MusicDetail
@login_required(login_url="/login")
def addtofavorit(request,*args,**kwargs):
    musicid=kwargs["musicid"]
    userid=request.user.id
    checkid=FavoritDetail.objects.check_id(userid)
    checkmusic=FavoritDetail.objects.filter(FavoritSong_id=musicid,DetailFavortiUser__FavoritUser_id=userid).values_list("FavoritSong__title").first()
    if checkmusic is not None:
        checkname=FavoritDetail.objects.filter(DetailFavortiUser__FavoritUser_id=userid,FavoritSong__title__contains=checkmusic[0][0])
        if checkname is None:
            newFavortiMusic=FavoritDetail.objects.create(FavoritSong_id=musicid,DetailFavortiUser_id=checkid.id)
    if checkmusic is None:
        newFavortiMusic = FavoritDetail.objects.create(FavoritSong_id=musicid, DetailFavortiUser_id=checkid.id)
        print(newFavortiMusic)
        listid=FavoritDetail.objects.filter(FavoritSong_id=musicid, DetailFavortiUser_id=checkid.id).values_list("FavoritSong_id")
        print(len(listid))
    Artistid=MusicDetail.objects.filter(musicname_id=musicid).values_list("Artistdetail__ArtistName").first()
    print(Artistid)
    return redirect("/Favorit")
@login_required(login_url="/login")
def Favoritpage(request,*args,**kwargs):
    userid=request.user.id
    FavoritSongs=FavoritDetail.objects.filter(DetailFavortiUser__FavoritUser_id=userid).values_list("FavoritSong_id")
    selected_song_delete_duplicate_item=[]
    FavoritMusicDetail=[]
    for g in FavoritSongs:
        selected_song_delete_duplicate_item.extend(MusicDetail.objects.filter(musicname_id=g[0]).values_list("Genredetail_id"))
    for i in FavoritSongs:
        selected_song_delete_duplicate_item.extend(MusicDetail.objects.filter(musicname_id=i[0]).values_list("Genredetail_id"))
        if len(selected_song_delete_duplicate_item)>1:
            selected_song_delete_duplicate_item=selected_song_delete_duplicate_item[0][0]
            genre=selected_song_delete_duplicate_item
            FavoritMusicDetail.extend(MusicDetail.objects.filter(musicname_id=i[0],Genredetail_id=genre).distinct())
            selected_song_delete_duplicate_item=[]
        else:
            FavoritMusicDetail.extend(MusicDetail.objects.filter(musicname_id=i[0]))
            selected_song_delete_duplicate_item=[]
    print(FavoritMusicDetail)
    context={"FavoritMusicDetail":FavoritMusicDetail}
    return render(request,"FavoritPage.html",context)
def DeleteFromFavorit(request,*args,**kwargs):
    userid=request.user.id
    musicid=kwargs["musicid"]
    deleted_favorit=FavoritDetail.objects.filter(DetailFavortiUser__FavoritUser_id=userid,FavoritSong_id=musicid).delete()
    return redirect("/Favorit")
# Create your views here.
