from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', views.track_form), #localhost:p#/employee/list
    path('list/', views.track_list)
]