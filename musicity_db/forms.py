from django import forms
from .models import Track

class TrackForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = ('name', 'duration', 'genre')
        labels = {
            'name':'Track Name',
            'duration': 'Track Length (sec)'
        }

    def __init__(self, *args, **kwargs):
        super(TrackForm, self).__init__(*args, **kwargs)
        #self.fields['artist_id'].empty_label = "Select"

class TrackDurationQueryForm(forms.Form):
    start_duration = forms.IntegerField(label="Start Time")
    end_duration = forms.IntegerField(label="End Time")