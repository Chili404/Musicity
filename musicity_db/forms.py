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