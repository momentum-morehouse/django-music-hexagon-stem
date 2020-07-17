from django.shortcuts import render
from .models import Album, Users

# Create your views here.
def index(request):
  all_albums = Album.objects.all()
  return render(request, 'mymusic/list_albums.html', context={'album':album})

# def add_albums(request):
#     if request.method == 'GET':
#         form = albumForm()
#     else:
#         form = albumForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_albums')

#     return render(request, "albums/add_albums.html", {"form": form})

# def delete_albums(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#     if request.method == 'POST':
#         album.delete()
#         return redirect(to='index')
#     return render(request, "albums/delete_albums.html", context={"album": album})