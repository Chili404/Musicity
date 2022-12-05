import logging, sys

from django.shortcuts import render,redirect
from django.db import connection
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
    original_stdout = sys.stdout # Save a reference to the original standard output

    form_time = TrackDurationQueryForm(request.POST or None)
    form_genre = TrackGenreQueryForm(request.POST or None)
    if request.method == "POST":
        if 'query_duration' in request.POST:
            form_time = TrackDurationQueryForm(request.POST)
            if form_time.is_valid():
                cursor=connection.cursor()
                statement = "call QueryDuration({0}, {1})".format(form_time.cleaned_data['start_duration'], form_time.cleaned_data['end_duration'])
                cursor.execute(statement)
                result = cursor.fetchall()
                track_list = Track.objects.filter( pk__in = (o[0] for o in result) )

        elif 'query_genre' in request.POST:
            form_genre = TrackGenreQueryForm(request.POST)
            if form_genre.is_valid():
                
                cursor=connection.cursor()
                statement = "call QueryGenre(\"{0}\")".format(form_genre.cleaned_data['genre'])
                cursor.execute(statement)
                result = cursor.fetchall()
                track_list = Track.objects.filter( pk__in = (o[0] for o in result) )
            
        #original_stdout = sys.stdout # Save a reference to the original standard output
        #with open('testing.txt', 'w') as f:
        #        sys.stdout = f # Change the standard output to the file we created.
        #        print(form)
        #        sys.stdout = original_stdout
    
    context = {'track_list': track_list, 'formTime':form_time, 'formGenre': form_genre}
    return render(request, "musicity_db/track_list.html", context)


def track_form(request, id=0):
    if request.method == "GET":
        if id == 0: #insert
            form = TrackForm()
        else: #update
            track = Track.objects.get(pk=id)
            form = TrackForm(instance=track)          
        return render(request, "musicity_db/track_form.html", {'form':form})
    else:
        if id == 0:
            form = TrackForm(request.POST)
        else:
            track = Track.objects.get(pk=id)
            form = TrackForm(request.POST, instance = track)
        if form.is_valid():
            form.save()
        return redirect('/musicity/track/')

def track_delete(request, id):
    track = Track.objects.get(pk=id)
    track.delete()
    return redirect('/musicity/track/')

def track_sort_asc(request, header):
    track_list = Track.objects.all().order_by(header)
    context = {'track_list':track_list}
    return render(request, "musicity_db/track_list.html", context)

def track_sort_dec(request, header):
    track_list = Track.objects.all().order_by(header)
    context = {'track_list':track_list}
    return render(request, "musicity_db/track_list.html", context)

# album 

def album_list(request):
    album_list = Album.objects.all().order_by('name')
    context = {'album_list':album_list}
    return render(request, "musicity_db/album_list.html", context)

def album_form(request, id=0):
    if request.method == "GET":
        if id == 0: #insert
            form = AlbumForm()
        else: #update
            album = Album.objects.get(pk=id)
            form = AlbumForm(instance=album)          
        return render(request, "musicity_db/album_form.html", {'form':form})
    else:
        if id == 0:
            form = AlbumForm(request.POST)
        else:
            album = Album.objects.get(pk=id)
            form = AlbumForm(request.POST, instance = album)
        if form.is_valid():
            form.save()
        return redirect('/musicity/album/')

def album_delete(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('/musicity/album/')

def album_sort_asc(request, header):
    album_list = Album.objects.all().order_by(header)
    context = {'album_list':album_list}
    return render(request, "musicity_db/album_list.html", context)

def album_sort_dec(request, header):
    album_list = Album.objects.all().order_by(header)
    context = {'album_list':album_list}
    return render(request, "musicity_db/album_list.html", context)