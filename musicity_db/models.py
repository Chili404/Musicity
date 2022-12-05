from django.db import models

# Create your models here.
# TO-DO
#   -Add Album Model


# class Label(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)

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
    )
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=2, choices=GENRES)
    #artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)


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
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    genre = models.CharField(max_length=2, choices=GENRES)
<<<<<<< HEAD
    #artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #album_id = models.ForeignKey(Album, on_delete=models.CASCADE) #Cascade means if corresponding album is deleted, track will be deleted too





=======
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # album_id = models.ForeignKey(Album, on_delete=models.CASCADE) #Cascade means if corresponding album is deleted, track will be deleted too
>>>>>>> de341e7 (Changed artist icon)
