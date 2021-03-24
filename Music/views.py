from random import sample

# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from Artist.models import Artist
from Favorit.models import FavoritDetail,FavoritMusic
from Music.models import Music,MusicDetail
from History_user.models import HistoryByuser
from download.models import DownloadDetail,DownloadSong
from Favorit.models import FavoritDetail,FavoritMusic
import mimetypes
# Create your views here.
def autoplayermusic(request,*args,**kwargs):
    musicfilename=kwargs["musicfile"]
    musicfile=Music.objects.filter(SongFile=musicfilename).filter()
    context={"musicfile":musicfile}
    return render(request,"artistsingle.html",context)
@method_decorator(login_required(login_url="/login"),name='dispatch')
class SearchMusic(LoginRequiredMixin,ListView):
    template_name = "SearchSongPage.html"
    def get_queryset(self):
        request=self.request
        searchedname=request.GET.get('q')
        userid=request.user.id
        print(searchedname)
        Search_Song=MusicDetail.objects.SearchSong(searchedname)
        selected_history=HistoryByuser.objects.filter(History_User_id=userid)
        if not selected_history:
            for i in Search_Song:
                selected_history = HistoryByuser.objects.create(History_User_id=userid, History_Song=i)
        else:
            for i in Search_Song:
                existed_history=HistoryByuser.objects.filter(History_User_id=userid,History_Song=i)
                if not existed_history:
                    for i in Search_Song:
                        selected_history=HistoryByuser.objects.create(History_User_id=userid,History_Song=i)
        return Search_Song
@login_required(login_url="/login")
def TopSong(request):
    user_song=FavoritMusic.objects.all().values_list("FavoritUser")
    listofuser=[]
    for i in user_song:
        listofuser.append(i[0])
    print("list_______of_____user")
    print(listofuser)
    get_user_song=[]
    Songs=[]
    selected_song=[]
    help_selected_song=[]
    for i in listofuser:
        Songs_start_user=FavoritDetail.objects.get_favorit_user_song(i)
        print(Songs_start_user)
        for j in range(1,len(listofuser)):
            print("j:")
            print(j)
            print("Jlistofuser")
            print(listofuser[j])
            Songs_user=FavoritDetail.objects.get_favorit_user_song(listofuser[j])
            print(Songs_user)
            if not  selected_song:
                print("hrllo")
                for x in Songs_start_user:
                    for y in Songs_user:
                        if x==y:
                            selected_song.append(x)
                        print(selected_song)
                        print("finishstep")
            else:
                print("enter")
                print("selected_song")
                print(selected_song)
                print("Song_user")
                print(Songs_user)
                for l in selected_song:
                    for h in Songs_user:
                        if l==h:
                            help_selected_song.append(l)
                            print("helpsong")
                            print(help_selected_song)
                selected_song=[]
                for m in help_selected_song:
                    selected_song.append(m)
                help_selected_song=[]

    my_selected_listof_song=list(dict.fromkeys(selected_song))
    print("my_selected_listof_song")
    print(my_selected_listof_song)
    SelectSong=[]
    print(selected_song)
    user_one_song=FavoritDetail.objects.get_favorit_user_song(listofuser[0])
    for k in my_selected_listof_song:
        for n in user_one_song:
            if k==n:
                SelectSong.extend(MusicDetail.objects.filter(musicname_id=k).distinct()[:15])
    print(SelectSong)
    if not selected_song:
        selected_song=MusicDetail.objects.all()[:15]
    TopArtist=[]
    for v in my_selected_listof_song:
        TopArtist.append(MusicDetail.objects.filter(musicname_id=v).values_list("Artistdetail_id").distinct())
    selected_Top_artist=[]
    for top in TopArtist:
        selected_Top_artist.extend(Artist.objects.filter(id=top[0][0]).distinct())
    print("top artist")
    print(list(dict.fromkeys(selected_Top_artist)))
    selected_Top_artist=list(dict.fromkeys(selected_Top_artist))
    context={"SelectSong":SelectSong,
             "TopArtists":selected_Top_artist}
    return render(request,"TopSongs.html",context)
def LastSong(request):
    last_song=Music.objects.all().order_by("-time_add")[:5]
    context={"lastsong":last_song}
    return render(request,"NewReleased.html",context)
def All_last_song(request):
    selected_last_song=Music.objects.all().order_by("-time_add")[:10]
    context={"selected_last_songs":selected_last_song}
    return render(request,"All_last_song.html",context)

@login_required(login_url="/login")
def OfferingSong(request):
    userid=request.user.id
    final_music=FavoritDetail.objects.get_offered_song_user(userid)
    final_music=sample(final_music,5)
    context={"final_music":final_music}
    return render(request,"OfferingSong.html",context)
