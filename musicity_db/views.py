from django.shortcuts import render
from .forms import TrackForm

# Create your views here.
def track_list(request):
    return render(request, "musicity_db/track_list.html")

def track_form(request):
    form = TrackForm()
    return render(request, "musicity_db/track_form.html", {'form':form})

def track_delete(request):
    return