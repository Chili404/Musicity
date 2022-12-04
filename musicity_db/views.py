from django.shortcuts import render,redirect
from .forms import TrackForm
from .models import Track
# Create your views here.
def home(request):

    return render(request, 'musicity_db/index.html')

def track_list(request):
    track_list = Track.objects.all().order_by('name', 'duration')
    #track_list = Track.objects.all().order_by('-duration')
    context = {'track_list':track_list}
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