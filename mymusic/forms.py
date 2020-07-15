from django import forms
from .models import Album

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist_name',
            'date_released',
            
        ]
        widgets = {'date_released': forms.SelectDateWidget()
        }
