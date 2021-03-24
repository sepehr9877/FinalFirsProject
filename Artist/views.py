from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Artist
from Music.models import MusicDetail, Music
from download.models import DownloadDetail
def artistspage(request):
    artist=Artist.objects.all()
    top_artist_downloads=DownloadDetail.objects.get_top_artist()
    selected_song=[]
    for i in top_artist_downloads:
        selected_song.append(MusicDetail.objects.filter(id=i).values_list("Artistdetail_id"))
    artist_top=[]
    artist_list_id=[]
    for s in selected_song:
        artist_list_id.append(s[0][0])
    selected_song=list(dict.fromkeys(artist_list_id))
    for a in selected_song:
        artist_top.extend(Artist.objects.filter(id=a))
    context={"Artists":artist,
             "selectedtopartists":artist_top}
    return render(request,"artists.html",context)
def allartistpage(request):
    allartist=Artist.objects.all()
    paginator=Paginator(allartist,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"page_obj":page_obj,
             "artists":allartist}
    return render(request,"AlllArtistPage.html",context)
def artistsingle(request,*args,**kwargs):
    artistname=kwargs["artistname"]
    ArtisSingle=MusicDetail.objects.get_artist_by_artistname(artistname)
    print(ArtisSingle)
    Artistmain=Artist.objects.filter(ArtistName__contains=artistname).first()
    relatedsongsartists=MusicDetail.objects.get_related_song_by_artist(artistname)
    print(Artistmain)
    print(relatedsongsartists)
    context={
        "artistname":artistname,
        "Artistmain":Artistmain,
        "ArtistsSingle":ArtisSingle,
        "relatedsongsartists":relatedsongsartists
    }
    return render(request,"artistsingle.html",context)
def select_for_artistpage(request,*args,**kwargs):
    musicid=kwargs["musicid"]
    Artist_detail=MusicDetail.objects.filter(musicname_id=musicid).values_list("Artistdetail__ArtistName")

    return redirect(f"/artist/{Artist_detail[0][0]}")
def MoreSingleSongArtist(request,*args,**kwargs):
    artistname=kwargs["artistname"]
    relatedgenre = MusicDetail.objects.get_genre_by_artistname(artistname)
    print(relatedgenre)
    paginator=Paginator(relatedgenre,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        "moremusics":relatedgenre,
        "page_obj":page_obj
    }
    return render(request,"MoreSingleArtistSong.html",context)


# Create your views here.
