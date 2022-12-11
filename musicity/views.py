from django.shortcuts import redirect

#Tests
def redirect_view(request):
    response = redirect('/musicity/')
    return response