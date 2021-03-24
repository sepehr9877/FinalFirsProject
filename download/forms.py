from django import forms


class playforms(forms.Form):
    MusicName=forms.CharField(max_length=150)