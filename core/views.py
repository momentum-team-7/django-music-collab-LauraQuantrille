from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Album
from .models import Artist
from .forms import ArtistForm
from .forms import AlbumForm

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'html/index.html',{'albums': albums})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request,'html/artist_list.html',{'artists': artists})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'html/album_detail.html', {'album': album })

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request,'html/artist_detail.html',{'artist': artist})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm()
    return render(request, 'html/add_artist.html', {'form': form})

def add_album(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AlbumForm()
    return render(request, 'html/add_album.html',{'form': form})