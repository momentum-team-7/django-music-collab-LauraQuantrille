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
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AlbumForm()
    return render(request, 'html/add_album.html',{'form': form})

def edit_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = ArtistForm(instance=artist)
    return render(request, 'html/edit_artist.html', {'form': form, 'artist':artist })

def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/')

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'html/edit_album.html', {'form': form, 'album': album })


