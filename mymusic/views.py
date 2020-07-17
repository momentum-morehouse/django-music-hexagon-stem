from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album

# Create your views here.
def index(request):
  all_albums = Album.objects.all()
  return render(request, "mymusic/list_albums.html", {"all_albums": all_albums})

def add_albums(request):
     if request.method == 'GET':
         form = albumForm()
     else:
         form = albumForm(data=request.POST)
         if form.is_valid():
             form.save()
             return redirect(to='list_albums')

     return render(request, "albums/add_albums.html", {"form": form})

def delete_albums(request, pk):
     all_albums = get_object_or_404(Album, pk=pk)
     if request.method == 'POST':
         all_albums.delete()
         return redirect(to='index')
     return render(request, "albums/delete_albums.html", context={"all_albums": all_albums})