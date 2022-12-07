import sys
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db import connection

# Create your views here.


def home(request):

    return render(request, 'musicity_db/index.html')

# track


def track_list(request):
    track_list = Track.objects.all().order_by('name', 'duration')
    form_time = TrackDurationQueryForm(request.POST or None)
    form_genre = TrackGenreQueryForm(request.POST or None)
    form_artist = TrackArtistQueryForm(request.POST or None)
    form_album = TrackAlbumQueryForm(request.POST or None)
    form_name = TrackNameQueryForm(request.POST or None)
    #form = TrackDurationQueryForm(request.POST or None)
    if request.method == "POST":
        if 'query_duration' in request.POST:
            form_time = TrackDurationQueryForm(request.POST)
            if form_time.is_valid():
                cursor = connection.cursor()
                statement = "call QueryDuration({0}, {1})".format(
                    form_time.cleaned_data['start_duration'], form_time.cleaned_data['end_duration'])
                cursor.execute(statement)
                result = cursor.fetchall()
                track_list = Track.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_genre' in request.POST:
            form_genre = TrackGenreQueryForm(request.POST)
            if form_genre.is_valid():
                cursor = connection.cursor()
                statement = "call QueryGenre(\"{0}\")".format(
                    form_genre.cleaned_data['genre'])
                cursor.execute(statement)
                result = cursor.fetchall()
                track_list = Track.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_artist' in request.POST:
            form_artist = TrackArtistQueryForm(request.POST)
            if form_artist.is_valid():
                cursor = connection.cursor()
                statement = "call QueryArtist(\"{0}\")".format(
                    form_artist.cleaned_data['artist_id'])
                cursor.execute(statement)
                result = cursor.fetchall()
                track_list = Track.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_album' in request.POST:
            form_album = TrackAlbumQueryForm(request.POST)
            if form_album.is_valid():
                cursor = connection.cursor()
                statement = "call QueryAlbum(\"{0}\")".format(
                    form_album.cleaned_data['album_id'])
                cursor.execute(statement)
                result = cursor.fetchall()
                track_list = Track.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_name' in request.POST:
            form_name = TrackNameQueryForm(request.POST)
            if form_name.is_valid():
                cursor = connection.cursor()
                statement = "call QueryName(\"{0}\")".format(
                    form_name.cleaned_data['name'])
                cursor.execute(statement)
                result = cursor.fetchall()
                track_list = Track.objects.filter(
                    pk__in=(o[0] for o in result))

        # original_stdout = sys.stdout # Save a reference to the original standard output
        # with open('testing.txt', 'w') as f:
        #        sys.stdout = f # Change the standard output to the file we created.
        #        print(form)
        #        sys.stdout = original_stdout

    context = {'track_list': track_list, 'formTime': form_time, 'formGenre': form_genre, 'formArtist': form_artist, 'formAlbum': form_album,
               'formName': form_name}
    #context = {'track_list': track_list, 'form':form}
    return render(request, "musicity_db/track/track_list.html", context)


def track_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = TrackForm()
        else:  # update
            track = Track.objects.get(pk=id)
            form = TrackForm(instance=track)
        return render(request, "musicity_db/track/track_form.html", {'form': form})
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
    return render(request, "musicity_db/track/track_list.html", context)


def track_sort_dec(request, header):
    track_list = Track.objects.all().order_by(header)
    context = {'track_list': track_list}
    return render(request, "musicity_db/track/track_list.html", context)


def stream_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = StreamForm()
        else:  # update
            stream = Streams.objects.get(track_id=id)
            form = StreamForm(instance=stream)
            track = Track.objects.get(pk=id)
        return render(request, "musicity_db/track/stream_form.html", {'form': form, 'track': track})
    else:
        if id == 0:
            form = StreamForm(request.POST)
        else:
            stream = Streams.objects.get(track_id=id)
            form = StreamForm(request.POST, instance=stream)
        if form.is_valid():
            form.save()
        return redirect('/musicity/track/')


# album


def album_list(request):
    album_list = Album.objects.all().order_by('name')
    form_name = AlbumNameQueryForm(request.POST or None)
    form_genre = AlbumGenreQueryForm(request.POST or None)
    form_artist = AlbumArtistQueryForm(request.POST or None)

    if request.method == "POST":
        if 'query_name' in request.POST:
            form_name = AlbumNameQueryForm(request.POST)
            if form_name.is_valid():
                cursor = connection.cursor()
                statement = "call QueryAlbumName(\"{0}\")".format(
                    form_name.cleaned_data['name'])
                cursor.execute(statement)
                result = cursor.fetchall()
                album_list = Album.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_genre' in request.POST:
            form_genre = AlbumGenreQueryForm(request.POST)
            if form_genre.is_valid():
                cursor = connection.cursor()
                statement = "call QueryAlbumGenre(\"{0}\")".format(
                    form_genre.cleaned_data['genre'])
                cursor.execute(statement)
                result = cursor.fetchall()
                album_list = Album.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_artist' in request.POST:
            form_artist = AlbumArtistQueryForm(request.POST)
            if form_artist.is_valid():
                cursor = connection.cursor()
                statement = "call QueryAlbumArtist(\"{0}\")".format(
                    form_artist.cleaned_data['artist_id'])
                cursor.execute(statement)
                result = cursor.fetchall()
                album_list = Album.objects.filter(
                    pk__in=(o[0] for o in result))

    context = {'album_list': album_list, 'formName': form_name,
               'formGenre': form_genre, 'formArtist': form_artist}
    return render(request, "musicity_db/album/album_list.html", context)


def album_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = AlbumForm()
        else:  # update
            album = Album.objects.get(pk=id)
            form = AlbumForm(instance=album)
        return render(request, "musicity_db/album/album_form.html", {'form': form})
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
    return render(request, "musicity_db/album/album_list.html", context)


def album_sort_dec(request, header):
    album_list = Album.objects.all().order_by(header)
    context = {'album_list': album_list}
    return render(request, "musicity_db/album/album_list.html", context)


# artist

def artist_list(request):
    artist_list = Artist.objects.all().order_by('name')
    form_artist = ArtistNameQueryForm(request.POST or None)
    form_location = ArtistLocationQueryForm(request.POST or None)
    form_label = ArtistLabelQueryForm(request.POST or None)

    if request.method == "POST":
        if 'query_artist_name' in request.POST:
            form_artist = ArtistNameQueryForm(request.POST)
            if form_artist.is_valid():
                cursor = connection.cursor()
                statement = "call QueryArtistName(\"{0}\")".format(
                    form_artist.cleaned_data['name'])
                cursor.execute(statement)
                result = cursor.fetchall()
                artist_list = Artist.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_artist_location' in request.POST:
            form_location = ArtistLocationQueryForm(request.POST)
            if form_location.is_valid():
                cursor = connection.cursor()
                statement = "call QueryArtistLocation(\"{0}\")".format(
                    form_location.cleaned_data['location'])
                cursor.execute(statement)
                result = cursor.fetchall()
                artist_list = Artist.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_artist_label' in request.POST:
            form_label = ArtistLabelQueryForm(request.POST)
            if form_label.is_valid():
                cursor = connection.cursor()
                statement = "call QueryArtistLabel(\"{0}\")".format(
                    form_label.cleaned_data['label_id'])
                cursor.execute(statement)
                result = cursor.fetchall()
                artist_list = Artist.objects.filter(
                    pk__in=(o[0] for o in result))

    context = {'artist_list': artist_list,
               'formArtist': form_artist, 'formLocation': form_location, 'formLabel': form_label}
    # context = {'artist_list': artist_list}
    return render(request, "musicity_db/artist/artist_list.html", context)


def artist_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = ArtistForm()
        else:  # update
            artist = Artist.objects.get(pk=id)
            form = ArtistForm(instance=artist)
        return render(request, "musicity_db/artist/artist_form.html", {'form': form})
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
    return render(request, "musicity_db/artist/artist_list.html", context)


def artist_sort_dec(request, header):
    artist_list = Artist.objects.all().order_by(header)
    context = {'artist_list': artist_list}
    return render(request, "musicity_db/artist/artist_list.html", context)

# label


def label_list(request):
    label_list = Label.objects.all().order_by('name')
    form_name = LabelNameQueryForm(request.POST or None)
    form_location = LabelLocationQueryForm(request.POST or None)

    if request.method == "POST":
        if 'query_name' in request.POST:
            form_name = LabelNameQueryForm(request.POST)
            if form_name.is_valid():
                cursor = connection.cursor()
                statement = "call QueryLabelName(\"{0}\")".format(
                    form_name.cleaned_data['name'])
                cursor.execute(statement)
                result = cursor.fetchall()
                label_list = Label.objects.filter(
                    pk__in=(o[0] for o in result))

        elif 'query_location' in request.POST:
            form_location = LabelLocationQueryForm(request.POST)
            if form_location.is_valid():
                cursor = connection.cursor()
                statement = "call QueryLabelLocation(\"{0}\")".format(
                    form_location.cleaned_data['location'])
                cursor.execute(statement)
                result = cursor.fetchall()
                label_list = Label.objects.filter(
                    pk__in=(o[0] for o in result))

    context = {'label_list': label_list,
               'formName': form_name, 'formLocation': form_location}
    return render(request, "musicity_db/label/label_list.html", context)


def label_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # insert
            form = LabelForm()
        else:  # update
            label = Label.objects.get(pk=id)
            form = LabelForm(instance=label)
        return render(request, "musicity_db/label/label_form.html", {'form': form})
    else:
        if id == 0:
            form = LabelForm(request.POST)
        else:
            label = Label.objects.get(pk=id)
            form = LabelForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
        return redirect('/musicity/label/')


def label_delete(request, id):
    label = Label.objects.get(pk=id)
    label.delete()
    return redirect('/musicity/label/')


def label_sort_asc(request, header):
    label_list = Label.objects.all().order_by(header)
    context = {'label_list': label_list}
    return render(request, "musicity_db/label/label_list.html", context)


def label_sort_dec(request, header):
    label_list = Label.objects.all().order_by(header)
    context = {'label_list': label_list}
    return render(request, "musicity_db/label/label_list.html", context)


def top_list(request):
    cursor = connection.cursor()
    statement = "call Top10()"
    cursor.execute(statement)
    result = cursor.fetchall()
    original_stdout = sys.stdout  # Save a reference to the original standard output
    with open('testing.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print(result)
        sys.stdout = original_stdout
    context = {'item_list': result}
    return render(request, "musicity_db/top/top_list.html", context)
