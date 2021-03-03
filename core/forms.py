from django import forms
from .models import Artist
from .models import Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist', 'label']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_date', 'photo']