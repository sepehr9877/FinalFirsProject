from django import forms
from .models import Add_PlayList,MusicFile
class PlayListForm(forms.ModelForm):
    class Meta:
        model=Add_PlayList
        fields=('PlayListName','PlayListImage')
class UserFormPlayList(forms.ModelForm):
    class Meta:
        model=MusicFile
        fields=('SongFile','AlbumName','ArtistName','SongName','is_paid')