from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('musicplayer',Mymusic.as_view(),name="mymusic"),
    path('songplay/<int:pk>',SongPlay.as_view(),name ='songplay'),
    path('search',Search.as_view(),name="search"),

]
