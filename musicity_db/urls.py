from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.track_form), #localhost:p#/employee/list
    path('list/', views.track_list)
]