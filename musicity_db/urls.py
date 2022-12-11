from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    # track urls
    # localhost:p#/employee/list
    path('track/', views.track_list, name="track_list"),
    path('track/form/', views.track_form, name="track_insert"),
    path('track/<int:id>/', views.track_form, name="track_update"),
    path('track/delete/<int:id>', views.track_delete, name="track_delete"),
    path('track/<str:header>', views.track_sort_asc, name="track_sort_asc"),
    path('track/<str:header>', views.track_sort_dec, name="track_sort_dec"),
    path('track/stream/<int:id>', views.stream_form, name="stream_update"),


    # album urls
    path('album/', views.album_list, name="album_list"),
    path('album/form/', views.album_form, name="album_insert"),
    path('album/<int:id>/', views.album_form, name="album_update"),
    path('album/delete/<int:id>/', views.album_delete, name="album_delete"),
    path('album/<str:header>', views.album_sort_asc, name="album_sort_asc"),
    path('album/<str:header>', views.album_sort_dec, name="album_sort_dec"),

    # artist urls
    path('artist/', views.artist_list, name="artist_list"),
    path('artist/form/', views.artist_form, name="artist_insert"),
    path('artist/<int:id>/', views.artist_form, name="artist_update"),
    path('artist/delete/<int:id>/', views.artist_delete, name="artist_delete"),
    path('artist/<str:header>', views.artist_sort_asc, name="artist_sort_asc"),
    path('artist/<str:header>', views.artist_sort_dec, name="artist_sort_dec"),

    # label urls
    path('label/', views.label_list, name='label_list'),
    path('label/form/', views.label_form, name="label_insert"),
    path('label/<int:id>/', views.label_form, name="label_update"),
    path('label/delete/<int:id>/', views.label_delete, name="label_delete"),
    path('label/<str:header>', views.label_sort_asc, name="label_sort_asc"),
    path('label/<str:header>', views.label_sort_dec, name="label_sort_dec"),

    #top urls
    path('top10/', views.top_list, name='top_list'),
    path('top10/<str:header>', views.label_sort_asc, name="label_sort_asc"),
    path('top10/<str:header>', views.label_sort_dec, name="label_sort_dec"),
]
