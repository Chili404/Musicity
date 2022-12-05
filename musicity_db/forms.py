from django import forms
from .models import *

class TrackForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = ('name', 'duration', 'genre')#, 'artist_id', 'album_id')
        labels = {
            'name':'Track Name',
            'duration': 'Track Length (sec)'
        }

    def __init__(self, *args, **kwargs):
        super(TrackForm, self).__init__(*args, **kwargs)
        #self.fields['artist_id'].empty_label = "Select"
        #self.fields['album_id'].empty_label = "Select"

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields = ('name', 'genre') #'artist_id')
        labels = {
            'name' : 'Album Name'
            #'artist_id' : 'Artist'
        }

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        #self.fields['artist_id'].empty_label = "Select"


class TrackDurationQueryForm(forms.Form):
    start_duration = forms.IntegerField(label="Start Time")
    end_duration = forms.IntegerField(label="End Time")

class TrackGenreQueryForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = ('genre',)