from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Album
from Music.models import MusicDetail,Music
def AlbumPage(request):
    album=Album.objects.all()
    musics=MusicDetail.objects.all()
    context={"albums":album,
             "Musics":musics}
    print(album)
    return render(request,"AlbumPage.html",context)
def AllSongs(request):
    All_Songs=MusicDetail.objects.all()
    paginator=Paginator(All_Songs,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"All_Sons":All_Songs,
             "page_obj":page_obj}
    return render(request,"AllSOngsPage.html",context)

def AlbumSinglePage(request,*args,**kwargs):
    albumname=kwargs["AlbumName"]
    musics=MusicDetail.objects.get_id_by_name(albumname)
    albumdetail=Album.objects.filter(AlbumName=albumname).first()
    artistdetail=MusicDetail.objects.get_artist(albumname)
    relatedalbum=MusicDetail.objects.get_relatedalbum_by_name(albumname)
    context={"musics":musics,
             "Albumdetail":albumdetail,
             "relatedalbum":relatedalbum,
             "albumname":albumname}
    return render(request,"SingleAlbum.html",context)
def ViewMoreSong(request,*args,**kwargs):
    albumname = kwargs["albumname"]
    relatedalbum = MusicDetail.objects.get_relatedalbum_by_name(albumname)
    paginator=Paginator(relatedalbum,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"relatedalbum":relatedalbum,
             "page_obj":page_obj}
    return render(request,"ViewMoreRelatedSong.html",context)
def allalbums(request):
    All_Albums=Album.objects.all()
    paginate=Paginator(All_Albums,6)
    page_number=request.GET.get("page")
    page_obj=paginate.get_page(page_number)
    context={"All_Albums":All_Albums,
             "page_obj":page_obj}
    return render(request,"All_ALbums.html",context)

# Create your views here.
