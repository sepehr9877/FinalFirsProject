from django.core.paginator import Paginator
from django.shortcuts import render
from .models import  Genre
from Music.models import MusicDetail
def genrepage(request):
    rock=Genre.objects.filter(NameGenre__contains="Rock").first()
    hiphop=Genre.objects.filter(NameGenre__contains="HipHop").first()
    classic=Genre.objects.filter(NameGenre__contains="Classic").first()
    love=Genre.objects.filter(NameGenre__contains="Love").first()
    print(love)
    EDm=Genre.objects.filter(NameGenre__contains="EDM").first()
    Happy=Genre.objects.filter(NameGenre__contains="Happy").first()
    print(Happy)
    Blooz=Genre.objects.filter(NameGenre__contains="Bloze").first()
    Cell=Genre.objects.filter(NameGenre__contains="sell").first()
    Single=Genre.objects.filter(NameGenre__contains="Single").first()
    metal=Genre.objects.filter(NameGenre__contains="Metal").first()
    Jazz=Genre.objects.filter(NameGenre__contains="Jazz").first()
    pop=Genre.objects.filter(NameGenre__contains="Pop").first()
    folk=Genre.objects.filter(NameGenre__contains="Folk").first()
    context={
        "rock":rock,
        "hiphop":hiphop,
        "classic":classic,
        "love":love,
        "EDM":EDm,
        "Happy":Happy,
        "Bloze":Blooz,
        "Cell":Cell,
        "Single":Single,
        "metal":metal,
        "jazz":Jazz,
        "pop":pop,
        "folk":folk
    }
    return render(request,"GenrePage.html",context)
def GenreSingle(request,*args,**kwargs):
    genrename=kwargs["genrename"]
    music=MusicDetail.objects.get_music_by_genre(genrename)
    context={"muiscs":music,
             "genrename":genrename}
    return render(request,"GenreSingle.html",context)
def GenreMore(reuqest,*args,**kwargs):
    genrename=kwargs["genrename"]
    moremusic=MusicDetail.objects.get_music_by_genre(genrename)
    paginator=Paginator(moremusic,6)
    page_number=reuqest.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        "genrename":genrename,
        "moremusics":moremusic,
        'page_obj':page_obj
    }
    return  render(reuqest,"GenreMore.html",context)