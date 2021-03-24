import os

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Music.models import Music, MusicDetail
from .forms import PlayListForm,UserFormPlayList
from .models import PlayListDetail, Add_PlayList, upload_song_user, MusicFile
from contact.models import Followers
following=True
accept=True
def handle_uploaded_file(f):
    with open('static_cdn/media_root/upload', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def get_filepath(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext
def uploading(filename):
    name,ext=get_filepath(filename)
    finalname=f"{name}{ext}"
    return f"Usersong/{finalname}"
def UploadSong(request):
    user_id=request.user.id
    NewPlaylist=PlayListForm(request.POST or request.FILES)
    UserPlaylist=UserFormPlayList(request.POST or request.FILES)
    if NewPlaylist.is_valid() and UserPlaylist.is_valid():
        PlayListName=NewPlaylist.cleaned_data.get("PlayListName")
        PlayListImage=request.FILES['PlayListImage']
        SongFile = request.FILES['SongFile']
        Songname=UserPlaylist.cleaned_data.get("SongName")
        ArtistName=UserPlaylist.cleaned_data.get("ArtistName")
        AlbumName=UserPlaylist.cleaned_data.get("AlbumName")
        Status=UserPlaylist.cleaned_data.get("is_paid")
        PlayList_ByUser=MusicFile.objects.create(SongName=Songname,SongFile=SongFile,ArtistName=ArtistName,AlbumName=AlbumName,is_paid=Status)
        AddtoPlayList=Add_PlayList.objects.create(PlayListName=PlayListName,PlayListImage=PlayListImage)
        userid=request.user.id
        User_PlayList=PlayListDetail.objects.create(UserPlayList_id=userid,PlayListSelect_id=AddtoPlayList.id,Music_File_id=PlayList_ByUser.id)
        return redirect("/")
    playlist__name=PlayListDetail.objects.filter(UserPlayList_id=user_id)
    context={"playlist":NewPlaylist,
             "UserPlayList":UserPlaylist,
             "playlist__name":playlist__name}
    return render(request, "UploadFIle.html", context)
@login_required(login_url="/login")
def PlayListPage(request):
    userid=request.user.id
    UserPlayListid=PlayListDetail.objects.filter(UserPlayList_id=userid).values_list("PlayListSelect_id").distinct()
    UserPlayList=[]
    for i in UserPlayListid:
        UserPlayList.extend(Add_PlayList.objects.filter(id=i[0]))
    selectedplaylist=PlayListDetail.objects.all().values_list("PlayListSelect_id").distinct()
    PlayLists=[]
    for x in selectedplaylist:
        PlayLists.extend(Add_PlayList.objects.filter(id=x[0]))
    print(PlayLists)
    context={"PlayLists":PlayLists,
             "UserPlaylist":UserPlayList}
    return render(request,"PlayListPage.html",context)
def AllPlayListPage(request):
    userid = request.user.id
    AllPlayLists = PlayListDetail.objects.all().distinct()
    print(AllPlayLists)
    context = {"AllPlayLists": AllPlayLists}
    return render(request, "AllPlaylListPage.html", context)
# Create your views here.
def AddToPlaylist_User(request,*args,**kwargs):
    playlistid=kwargs["ID"]
    userid=request.user.id
    userplaylist=PlayListDetail.objects.filter(UserPlayList_id=userid,PlayListSelect_id=playlistid).first()

    playlistoption=Add_PlayList.objects.filter(id=playlistid).first()
    selected_form=UserFormPlayList(request.POST or request.FILES)
    if selected_form.is_valid():
        SongFile=request.FILES['SongFile']
        AlbumName=selected_form.cleaned_data.get("AlbumName")
        ArtistName=selected_form.cleaned_data.get("ArtistName")
        SongName=selected_form.cleaned_data.get("SongName")
        addsonguser =MusicFile.objects.create(SongFile=SongFile,AlbumName=AlbumName,ArtistName=ArtistName,SongName=SongName)
        user_song_playlist=PlayListDetail.objects.create(UserPlayList_id=userid,PlayListSelect_id=playlistid,Music_File_id=addsonguser.id)
        return redirect("/")
    context={"selected_form":selected_form,
             "userplaylist":userplaylist}
    return render(request,"selected_playlist.html",context)
def showplaylist(request,*args,**kwargs):
    playlistid=kwargs["ID"]
    userid=request.user.id
    selectingplaylist=PlayListDetail.objects.filter(PlayListSelect_id=playlistid).first()
    selected_songid=PlayListDetail.objects.filter(PlayListSelect_id=playlistid).distinct().values_list("Music_File")
    print(selected_songid)
    selected_song=[]
    for i in selected_songid:
        selected_song.extend(MusicFile.objects.filter(id=i[0]))
    print(selected_song)
    user_to=PlayListDetail.objects.filter(PlayListSelect_id=playlistid).values_list("UserPlayList_id")
    user_to_id=[]
    print("ioo")
    print(user_to)
    for i in user_to:
        user_to_id.append(i[0])
    showiconfollow=Followers.objects.filter(from_user_id=userid,to_user_id=user_to_id[0])
    print("show")
    print(showiconfollow)
    accept_by_user=Followers.objects.filter(from_user_id=userid,to_user_id=user_to_id[0],accept_by_user=False)
    print("accep")
    print(accept_by_user)
    global following
    global accept
    if showiconfollow:
        following=True
        if accept_by_user:
            accept=False
        else:
            accept=True
    else:
        following=False
    context={"selected_plalists":selectingplaylist,
             "selected_song":selected_song,
             "playlistid":playlistid,
             "accept": accept,
             "following":following}
    return render(request,"SinglePlaylist.html",context)
def showmyplaylist(request,*args,**kwargs):
    playlistid=kwargs["playlistid"]
    myplaylist=Add_PlayList.objects.filter(id=playlistid).first()
    userid=request.user.id
    selected_playlist=PlayListDetail.objects.filter(UserPlayList_id=userid,PlayListSelect_id=playlistid)
    context={"selected_playlists":selected_playlist,
             "Playlistid":playlistid,
             "myplaylist":myplaylist}
    return render(request,"ShowMyPlaylist.html",context)
def deletefromplaylist(request,*args,**kwargs):
    userid=request.user.id
    musicid=kwargs["musicid"]
    print(musicid)
    playlistid=kwargs["ID"]
    print(playlistid)
    delete_music=PlayListDetail.objects.filter(UserPlayList_id=userid,PlayListSelect_id=playlistid,Music_File_id=musicid).delete()
    select_playlist=PlayListDetail.objects.filter(UserPlayList_id=userid,PlayListSelect_id=playlistid)
    if len(select_playlist)==0:
        select_playlist.delete()
        return redirect("/Playlist")
    return redirect(f"/playlist/{playlistid}")
def AddedPlaylist(request,*args,**kwargs):
    playlistid=kwargs["ID"]
    userid=request.user.id
    music=PlayListDetail.objects.filter(PlayListSelect_id=playlistid).values_list("Music_File").distinct()
    print(music)
    addmusic_user=[]
    for i in music:
        PlayListDetail.objects.create(UserPlayList_id=userid,Music_File_id=i[0],PlayListSelect_id=playlistid)
    return redirect("/Playlist")
def chooseplaylist(request,*args,**kwargs):
    musicid=kwargs["musicid"]
    userid=request.user.id
    selectplaylists=PlayListDetail.objects.filter(UserPlayList_id=userid).values_list("PlayListSelect_id")
    playlists=[]
    selectplaylists=list(dict.fromkeys(selectplaylists))
    for i in selectplaylists:
        playlists.extend(Add_PlayList.objects.filter(id=i[0]))
    context={"playlists":playlists,
             "musicid":musicid}
    return render(request,"chooseyourplaylist.html",context)
def AddToSelectedPlaylist(request,*args,**kwargs):
    favoritmusicid=kwargs["musicid"]
    print(favoritmusicid)
    userid=request.user.id
    print(userid)
    selected_from_music=MusicDetail.objects.filter(musicname_id=favoritmusicid).values_list("musicname__SongFile",
                                                                                            "musicname__title",
                                                                                            "Artistdetail__ArtistName",
                                                                                            "albumdetail__AlbumName").first()
    print("selected_from_music")
    print(selected_from_music)
    playlistname=kwargs["name"]
    print(playlistname)
    selectplaylist=PlayListDetail.objects.get_playlist_byname(playlistname,userid).values_list("PlayListSelect_id")
    print("selectplalist")
    print(selectplaylist)
    selectidfrom_playlist=[]
    for i in selectplaylist:
        selectidfrom_playlist.append(i[0])
    print("selectidfrom_playlist")
    print(selectidfrom_playlist)
    selected_name=MusicFile.objects.filter(SongName=selected_from_music[1],SongFile=selected_from_music[0]).values_list("id")
    print("selected_name")
    print(selected_name)
    if  selected_name:
        song_user=PlayListDetail.objects.filter(UserPlayList_id=userid,PlayListSelect_id=selectidfrom_playlist[0],Music_File__SongFile=selected_from_music[0],Music_File__SongName__contains=selected_from_music[1]).first()
        print("songuser")
        print(song_user)
        print("f")
        if not song_user:
            print("enter ")
            print(song_user)
            music_create = MusicFile.objects.create(SongFile=selected_from_music[0],
                                                    SongName=selected_from_music[1],
                                                    ArtistName=selected_from_music[2],
                                                    AlbumName=selected_from_music[3],
                                                    is_paid=True)
            addtoplaylist = PlayListDetail.objects.create(UserPlayList_id=userid,
                                                          PlayListSelect_id=selectidfrom_playlist[0],
                                                          Music_File_id=music_create.id)
            return redirect(f"/playlist/{selectplaylist[0][0]}")

        else:
            return redirect(f"/playlist/{selectplaylist[0][0]}")
    else:
        music_create = MusicFile.objects.create(SongFile=selected_from_music[0],
                                                SongName=selected_from_music[1],
                                                ArtistName=selected_from_music[2],
                                                AlbumName=selected_from_music[3])
        addtoplaylist = PlayListDetail.objects.create(UserPlayList_id=userid,
                                                      PlayListSelect_id=selectidfrom_playlist[0],
                                                      Music_File_id=music_create.id)
        return redirect(f"/playlist/{selectplaylist[0][0]}")
def deleteplaylist(request,*args,**kwargs):
    playlistid=kwargs["playlistid"]
    userid=request.user.id
    delete_addplaylist=Add_PlayList.objects.filter(id=playlistid).delete()
    deleted_playist=PlayListDetail.objects.filter(UserPlayList_id=userid,PlayListSelect_id=playlistid).delete()
    return redirect("/Playlist")
def modalcontent(request,*args,**kwargs):
    userid=request.user.id
    selected_playlists=PlayListDetail.objects.filter(UserPlayList_id=userid).values_list("PlayListSelect_id")
    selected_playlists=list(dict.fromkeys(selected_playlists))
    print("selected_playlists")
    print(selected_playlists)
    selectedplaylists=[]
    for i in selected_playlists:
        selectedplaylists.extend(Add_PlayList.objects.filter(id=i[0]))
    musicid=MusicDetail.objects.filter(musicname_id=1)
    context={"Playlists":selectedplaylists,
             "musicid":musicid}
    return render(request, "modalcontent.html", context)
def modal_playlist(request):
    userid = request.user.id
    selected_playlists = PlayListDetail.objects.filter(UserPlayList_id=userid).values_list("PlayListSelect_id")
    selected_playlists = list(dict.fromkeys(selected_playlists))
    print("selected_playlists")
    print(selected_playlists)
    selectedplaylists = []
    for i in selected_playlists:
        selectedplaylists.extend(Add_PlayList.objects.filter(id=i[0]))
    musicid = MusicDetail.objects.filter(musicname_id=1)
    context = {"Playlists": selectedplaylists,
               "musicid": musicid}
    return render(request,"modal_playlist.html",context)
def Add_Song_From_Favorit(request,*args,**kwargs):
    songid=kwargs["songid"]
    playlistid=kwargs["playlistid"]
    userid=request.user.id
    selectsong=MusicDetail.objects.filter(musicname_id=songid).values_list("musicname__title",
                                                                                  "Artistdetail__ArtistName",
                                                                                  "albumdetail__AlbumName",
                                                                                  "musicname__SongFile")
    list_selectsong=[]
    for i in selectsong:
        list_selectsong.extend(i)
    print("list_selectsong")
    print(list_selectsong[1])
    exist_song_=PlayListDetail.objects.filter(Music_File__SongName=list_selectsong[0],
                                         Music_File__ArtistName=list_selectsong[1],
                                         Music_File__AlbumName=list_selectsong[2],
                                         Music_File__SongFile=list_selectsong[3]).values_list("Music_File_id")
    list_existed_songfile=[]
    if exist_song_:
        for i in exist_song_:
            list_existed_songfile.append(i[0])
        existed_song_in_userplaylist = PlayListDetail.objects.filter(UserPlayList_id=userid,
                                                                     PlayListSelect_id=playlistid,
                                                                    Music_File_id=list_existed_songfile[0])
        if existed_song_in_userplaylist:
            return redirect("/Playlist")
        else:
            existed_song_in_userplaylist=PlayListDetail.objects.create(UserPlayList_id=userid,PlayListSelect_id=playlistid,Music_File_id=list_existed_songfile[0])
            return redirect("/Playlist")
    else:
        create_newMusicFile=MusicFile.objects.create(SongName=list_selectsong[0],ArtistName=list_selectsong[1],AlbumName=list_selectsong[2],SongFile=list_selectsong[3],is_favorit=True)
        add_to_user_playlist=PlayListDetail.objects.create(UserPlayList_id=userid,PlayListSelect_id=playlistid,Music_File_id=create_newMusicFile.id)
        return redirect("/Playlist")

def Add_Song_From_Playlist(request,*args,**kwargs):
    songid=kwargs["songid"]
    playlistid=kwargs["playlistid"]
    userid=request.user.id
    add_to_user = PlayListDetail.objects.filter(UserPlayList_id=userid, PlayListSelect_id=playlistid,Music_File_id=songid)
    if not add_to_user:
        add_to_user=PlayListDetail.objects.create(UserPlayList_id=userid,PlayListSelect_id=playlistid,Music_File_id=songid)
        return redirect("/Playlist")
    return redirect("/Playlist")
def showallplaylists(request):
    allplaylists=Add_PlayList.objects.all()
    paginator=Paginator(allplaylists,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"allplaylists":allplaylists,
             "page_obj":page_obj}
    return render(request,"viewallplaylists.html",context)