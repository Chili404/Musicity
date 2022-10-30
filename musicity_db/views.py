from django.shortcuts import render

# Create your views here.
def track_list(request):
    return render(request, "musicity_db/track_list.html")

def track_form(request):
    return render(request, "musicity_db/track_form.html")

def track_delete(request):
    return