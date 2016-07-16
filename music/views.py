from django.shortcuts import render
from music.models import Artista, Album, Track

def artistas(request):

    artistas = Artista.objects.all().order_by('orden')
    return render(request, 'artistas.html', {'artistas':artistas})


def albumes_por_artista(request,artista_id):

    albumes = Album.objects.filter(artista__id=artista_id)
    return render(request, 'albumes.html', {'albumes':albumes})


def tracks_por_album(request,album_id):

    tracks = Track.objects.filter(album__id=album_id)
    return render(request, 'tracks.html', {'tracks':tracks})
