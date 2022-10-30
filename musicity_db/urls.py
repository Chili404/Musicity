from django.urls import path,include
from . import views
urlpatterns = [
    path('track/', views.track_list), #localhost:p#/employee/list
    path('track/form/', views.track_form)
]