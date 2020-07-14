from django.shortcuts import render
from .models import Album, Users

# Create your views here.
def list_albums(request):
  albums = Album.objects.all()
  return render(request, 'albums/list_albums.html', context={'albums':albums})