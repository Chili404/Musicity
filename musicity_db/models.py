from django.db import models

# Create your models here.
# TO-DO
#   -Add Album Model


class Label(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    label_id = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Album(models.Model):
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
        ('e', 'experimental'),
        ('na', 'N/A')
    )
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=2, choices=GENRES)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
        ('e', 'experimental'),
        ('na', 'N/A')
    )
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    genre = models.CharField(max_length=2, choices=GENRES)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True) #Cascade means if corresponding album is deleted, track will be deleted too

    def __str__(self):
        return self.name
