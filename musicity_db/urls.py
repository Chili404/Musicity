from django.urls import path,include
from . import views
urlpatterns = [
    path('track/', views.track_list, name="track_list"), #localhost:p#/employee/list
    path('track/form/', views.track_form, name="track_insert"),
    path('track/<int:id>/', views.track_form, name="track_update"),
    path('track/delete/<int:id>', views.track_delete, name="track_delete")
]