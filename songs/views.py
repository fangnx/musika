from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Song
from .forms import SongForm

# Create your views here.
def song_list(request):
    queryset = Song.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'home.html', context)

def song_detail(request, id):
    instance = get_object_or_404(Song, id=id)
    context = {
        'title': instance.title,
        'instance': instance
    }
    return render(request, 'song_detail.html', context)

def song_create(request):
    form = SongForm(request.POST or None)
    # if request.method == 'POST':
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        'form': form,
    }
    return render(request, 'song_form.html', context)

def song_update(request):
    return render(request, 'home.html')

def song_delete(request):
    return render(request, 'home.html')
