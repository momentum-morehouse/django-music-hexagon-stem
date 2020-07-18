from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist_name',
            'date_released',
        ]
        widgets = {'date_released': forms.SelectDateWidget()
        }
