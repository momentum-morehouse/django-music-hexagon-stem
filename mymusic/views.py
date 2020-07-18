#from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.
def index(request):
  all_albums = Album.objects.all()
  return render(request, "mymusic/list_albums.html", {"all_albums": all_albums})

def add_albums(request):
     if request.method == 'GET':
         form = AlbumForm()
     else:
         form = AlbumForm(data=request.POST)
         if form.is_valid():
             form.save()
             return redirect(to='list_albums')

     return render(request, "mymusic/add_albums.html", {"form": form})

def delete_albums(request, pk):
     album = get_object_or_404(Album, pk=pk)
     if request.method == 'POST':
         album.delete()
         return redirect(to='index')
     return render(request, "mymusic/delete_albums.html", context={"album": album})