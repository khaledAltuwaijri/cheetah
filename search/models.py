from django.db import models

# Create your models here.
class UserProfile(models.Model):
    display_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    tracks = models.ManyToManyField('Song', through="PlaylistTrack")
    length = models.IntegerField(default=0)

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey('search.Playlist', on_delete=models.CASCADE)
    song = models.ForeignKey('search.Song', on_delete=models.CASCADE)
    position = models.IntegerField(default=0) #TODO: This default may need to change

    # class Meta:
    #     ordering= ['position']
