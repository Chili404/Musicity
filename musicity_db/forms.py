from django import forms
from .models import *


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('name', 'duration', 'genre', 'artist_id', 'album_id')
        labels = {
            'name': 'Track Name',
            'duration': 'Track Length (sec)',
            'artist_id': 'Artist',
            'album_id': 'Album'
        }

    def __init__(self, *args, **kwargs):
        super(TrackForm, self).__init__(*args, **kwargs)
        self.fields['artist_id'].empty_label = "Select"
        self.fields['album_id'].empty_label = "Select"

class TrackDurationQueryForm(forms.Form):
    start_duration = forms.IntegerField(label="Start Time")
    end_duration = forms.IntegerField(label="End Time")

class TrackGenreQueryForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = ('genre',)

class TrackArtistQueryForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = ('artist_id',)
        labels = {
            'artist_id' : 'Artist'
        }

class TrackAlbumQueryForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = ('album_id',)
        labels = {
            'album_id' : 'Album'
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'genre', 'release_date', 'artist_id')
        labels = {
            'name': 'Album Name',
            'artist_id': 'Artist',
            'release_date': 'Release Date'
        }

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['artist_id'].empty_label = "Select"

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'location', 'label_id')
        labels = {
            'name': 'Artist Name',
            'location': 'Location',
            'label_id': 'Label'
        }

    def __init__(self, *args, **kwargs):
        super(ArtistForm, self).__init__(*args, **kwargs)
        # self.fields['artist_id'].empty_label = "Select"

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name', 'location')
        labels = {
            'name' : 'Label Name',
            'location' : 'Location'
        }
    def __init__(self, *args, **kwargs):
        super(LabelForm, self).__init__(*args, **kwargs)