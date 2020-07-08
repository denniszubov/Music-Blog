from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=50)
    # audio_file = ...
    # tags = list field
    # cover_art = ...

    def __str__(self):
        return f"{self.song_name} by {self.artist}"
