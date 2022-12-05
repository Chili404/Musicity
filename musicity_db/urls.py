from django.urls import path,include
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),

    # track urls
    path('track/', views.track_list, name="track_list"), #localhost:p#/employee/list
    path('track/form/', views.track_form, name="track_insert"),
    path('track/<int:id>/', views.track_form, name="track_update"),
    path('track/delete/<int:id>', views.track_delete, name="track_delete"),
    path('track/<str:header>', views.track_sort_asc, name="track_sort_asc"),
    path('track/<str:header>', views.track_sort_dec, name="track_sort_dec"),

    # album urls
    path('album/', views.album_list, name="album_list"),
    path('album/form/', views.album_form, name="album_insert"),
    path('album/<int:id>/', views.album_form, name="album_update"),
    path('album/delete/<int:id>/', views.album_delete, name="album_delete"),
    path('album/<str:header>', views.album_sort_asc, name="album_sort_asc"),
    path('album/<str:header>', views.album_sort_dec, name="album_sort_dec")
]