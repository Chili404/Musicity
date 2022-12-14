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


class TrackNameQueryForm(forms.Form):
    name = forms.CharField(label="Enter Track Name")


class TrackDurationQueryForm(forms.Form):
    start_duration = forms.IntegerField(label="Start Time")
    end_duration = forms.IntegerField(label="End Time")


class TrackGenreQueryForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('genre',)


class TrackArtistQueryForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('artist_id',)
        labels = {
            'artist_id': 'Artist'
        }


class StreamForm(forms.ModelForm):
    class Meta:
        model = Streams
        fields = {'streams', }

    def __init__(self, *args, **kwargs):
        super(StreamForm, self).__init__(*args, **kwargs)
        self.fields['streams'].empty_label = 0


class TrackAlbumQueryForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('album_id',)
        labels = {
            'album_id': 'Album'
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


class AlbumNameQueryForm(forms.Form):
    name = forms.CharField(label="Enter Album Name")


class AlbumGenreQueryForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('genre',)


class AlbumArtistQueryForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist_id',)
        labels = {
            'artist_id': 'Artist'
        }


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


class ArtistNameQueryForm(forms.Form):
    name = forms.CharField(label="Enter Artist Name")


class ArtistLocationQueryForm(forms.Form):
    location = forms.CharField(label="Enter Artist Location")


class ArtistLabelQueryForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('label_id',)
        labels = {
            'label_id': 'Label'
        }


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name', 'location')
        labels = {
            'name': 'Label Name',
            'location': 'Location'
        }

    def __init__(self, *args, **kwargs):
        super(LabelForm, self).__init__(*args, **kwargs)


class LabelNameQueryForm(forms.Form):
    name = forms.CharField(label="Enter Label Name")


class LabelLocationQueryForm(forms.Form):
    location = forms.CharField(label="Enter Label Location")
