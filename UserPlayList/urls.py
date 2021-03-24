from django.urls import path
from .views import UploadSong, PlayListPage, AllPlayListPage, AddToPlaylist_User, showplaylist, \
    AddedPlaylist, chooseplaylist, AddToSelectedPlaylist, deletefromplaylist, deleteplaylist, modalcontent, \
    modal_playlist, Add_Song_From_Playlist,Add_Song_From_Favorit,showmyplaylist,showallplaylists

urlpatterns=[
    path("Playlist",PlayListPage),
    path('AddPlayList',UploadSong),
    path('Allplaylist',AllPlayListPage),
    path("AddToPlaylist/<ID>",AddToPlaylist_User),
    path("deleteplaylist/<playlistid>",deleteplaylist),
    path("playlist/<ID>",showplaylist),
    path("viewallplaylists",showallplaylists),
    path("ShowMyPlaylist/<playlistid>",showmyplaylist),
    path("AddToPlaylList/<ID>",AddedPlaylist),
    path("ChoosePlayList/<musicid>",chooseplaylist),
    path("AddToSelectedPlaylist/<name>/<musicid>",AddToSelectedPlaylist),
    path("deletefromplaylist/<ID>/<musicid>",deletefromplaylist),
    path("modalcontent",modalcontent,name="modalcontent"),
    path("modal_playlist",modal_playlist,name="modal_playlist"),
    path("Add_Song_From_Playlist/<songid>/<playlistid>",Add_Song_From_Playlist),
    path("Add_Song_From_Favorit/<songid>/<playlistid>",Add_Song_From_Favorit)
]