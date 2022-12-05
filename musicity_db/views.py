from django.shortcuts import render, redirect
from .forms import *
from .forms import TrackDurationQueryForm
from .models import *
# Create your views here.


def home(request):

    return render(request, 'musicity_db/index.html')

# track


def track_list(request):
    track_list = Track.objects.all().order_by('name', 'duration')
    #track_list = Track.objects.all().order_by('-duration')
    context = {'track_list': track_list}
    return render(request, "musicity_db/track_list.html", context)


def track_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = TrackForm()
        else:  # update
            track = Track.objects.get(pk=id)
            form = TrackForm(instance=track)
        return render(request, "musicity_db/track_form.html", {'form': form})
    else:
        if id == 0:
            form = TrackForm(request.POST)
        else:
            track = Track.objects.get(pk=id)
            form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
        return redirect('/musicity/track/')


def track_delete(request, id):
    track = Track.objects.get(pk=id)
    track.delete()
    return redirect('/musicity/track/')


def track_sort_asc(request, header):
    track_list = Track.objects.all().order_by(header)
    context = {'track_list': track_list}
    return render(request, "musicity_db/track_list.html", context)


def track_sort_dec(request, header):
    track_list = Track.objects.all().order_by(header)
    context = {'track_list': track_list}
    return render(request, "musicity_db/track_list.html", context)

# album


def album_list(request):
    album_list = Album.objects.all().order_by('name')
    context = {'album_list': album_list}
    return render(request, "musicity_db/album_list.html", context)


def album_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = AlbumForm()
        else:  # update
            album = Album.objects.get(pk=id)
            form = AlbumForm(instance=album)
        return render(request, "musicity_db/album_form.html", {'form': form})
    else:
        if id == 0:
            form = AlbumForm(request.POST)
        else:
            album = Album.objects.get(pk=id)
            form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
        return redirect('/musicity/album/')


def album_delete(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('/musicity/album/')


def album_sort_asc(request, header):
    album_list = Album.objects.all().order_by(header)
    context = {'album_list': album_list}
    return render(request, "musicity_db/album_list.html", context)


def album_sort_dec(request, header):
    album_list = Album.objects.all().order_by(header)
    context = {'album_list': album_list}
    return render(request, "musicity_db/album_list.html", context)


# artist

def artist_list(request):
    artist_list = Artist.objects.all().order_by('name')
    context = {'artist_list': artist_list}
    return render(request, "musicity_db/artist_list.html", context)


def artist_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = ArtistForm()
        else:  # update
            artist = Artist.objects.get(pk=id)
            form = ArtistForm(instance=artist)
        return render(request, "musicity_db/artist_form.html", {'form': form})
    else:
        if id == 0:
            form = ArtistForm(request.POST)
        else:
            artist = Artist.objects.get(pk=id)
            form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
        return redirect('/musicity/artist/')


def artist_delete(request, id):
    artist = Artist.objects.get(pk=id)
    artist.delete()
    return redirect('/musicity/artist/')


def artist_sort_asc(request, header):
    artist_list = Artist.objects.all().order_by(header)
    context = {'artist_list': artist_list}
    return render(request, "musicity_db/artist_list.html", context)


def artist_sort_dec(request, header):
    artist_list = Artist.objects.all().order_by(header)
    context = {'artist_list': artist_list}
    return render(request, "musicity_db/artist_list.html", context)
