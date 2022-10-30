from django import forms
from .models import Track

class TrackForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = ('name', 'duration', 'genre', 'artist_id')
        labels = {
            'name':'Track Name',
            'duration': 'Track Length (sec)',
            'artist_id': 'Artist'
        }

    def __init__(self, *args, **kwargs):
        super(TrackForm, self).__init__(*args, **kwargs)
        self.fields['artist_id'].empty_label = "Select"