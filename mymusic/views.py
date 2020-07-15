from django.shortcuts import render
from .models import Album

# Create your views here.
def list_albums(request):
  albums = Album.objects.all()
  return render(request, 'mymusic/list_albums.html', context={'albums':albums})