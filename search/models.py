from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class UserProfile(models.Model):
    display_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

class SearchTrack(models.Model):
    spotifyID = models.CharField(max_length=200)

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField(default=0)
    # songs = models.ArrayField(PlaylistTrack())


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    length_ms = models.IntegerField()
