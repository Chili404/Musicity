import logging, sys

from django.shortcuts import render,redirect
from django.db import connection
from .forms import TrackForm
from .forms import TrackDurationQueryForm
from .models import Track
# Create your views here.
def home(request):

    return render(request, 'musicity_db/index.html')

def track_list(request):
    track_list = Track.objects.all().order_by('name', 'duration')
    #track_list = Track.objects.all().order_by('-duration')
    form = TrackDurationQueryForm(request.POST or None)
    if request.method == "POST":
        form = TrackDurationQueryForm(request.POST)
        if form.is_valid():
            cursor=connection.cursor()
            statement = "call QueryDuration({0}, {1})".format(form.cleaned_data['start_duration'], form.cleaned_data['end_duration'])
            cursor.execute(statement)
            result = cursor.fetchall()
            track_list = Track.objects.filter( pk__in = (o[0] for o in result) )
            
        #original_stdout = sys.stdout # Save a reference to the original standard output
        #with open('testing.txt', 'w') as f:
        #        sys.stdout = f # Change the standard output to the file we created.
        #        print(form)
        #        sys.stdout = original_stdout
    
    context = {'track_list': track_list, 'form':form}
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

def track_query_duration(request, start_time, end_time):
    cursor=connection.cursor()
    statement = "call QueryDuration({0}, {1})".format(start_time, end_time)
    cursor.execute(statement)
    result = cursor.fetchall()
    return render(result, "musicity_db/track_list.html", {'QueryDuration':results})