from django.urls import path,include
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('track/', views.track_list, name="track_list"), #localhost:p#/employee/list
    path('track/form/', views.track_form, name="track_insert"),
    path('track/<int:id>/', views.track_form, name="track_update"),
    path('track/delete/<int:id>', views.track_delete, name="track_delete"),
    path('track/<str:header>', views.track_sort_asc, name="track_sort_asc"),
    path('track/<str:header>', views.track_sort_dec, name="track_sort_dec")
]