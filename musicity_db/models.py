from django.db import models

# Create your models here.
#TO-DO
#   -Add Album Model
#   -Add Artist Model
class Track(models.Model):
    GENRES = (
        ('r', 'rock'),
        ('j', 'jazz'),
        ('cl', 'classical'),
        ('p', 'pop'),
        ('rb', 'r&b'),
        ('c', 'country'),
        ('hh', 'hip-hop'),
        ('e', 'dance/electronic'),
        ('l', 'latin'),
    )
    name = models.CharField(max_length=100);
    duration = models.IntegerField();
    genre = models.CharField(max_length=2, choices=GENRES)
    #artist_id = models.ForeignKey(Artist)
    #album_id = models.ForeignKey(Album, on_delete=models.CASCADE) #Cascade means if corresponding album is deleted, track will be deleted too