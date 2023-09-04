from django.urls import path

from . import views

app_name = "mainApp"
urlpatterns = [
    path('', views.index, name="index"),
    path('homepage', views.homepage, name="homepage"),
    path('access/', views.access_room, name='access_room'),
    path('<str:room_name>/', views.room_name, name="room_name")
]