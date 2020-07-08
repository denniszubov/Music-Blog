from django.shortcuts import render
from django.views.generic import ListView
from .models import Song


# Create your views here.
class SongListView(ListView):
    model = Song
    template_name = "music/song_list.html"
    context_object_name = "songs"
