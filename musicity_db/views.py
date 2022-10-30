from django.shortcuts import render,redirect
from .forms import TrackForm
from .models import Track
# Create your views here.
def track_list(request):
    context = {'track_list':Track.objects.all()}
    return render(request, "musicity_db/track_list.html", context)

def track_form(request):
    if request.method == "GET":
        form = TrackForm()
        return render(request, "musicity_db/track_form.html", {'form':form})
    else:
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('musicity/track/')

def track_delete(request):
    return