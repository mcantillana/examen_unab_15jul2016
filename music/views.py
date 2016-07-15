from django.shortcuts import render
from music.models import Artista

def artistas(request):

    artistas = Artista.objects.all().order_by('orden')
    return render(request, 'artistas.html', {'artistas':artistas})


# def albumes_por_artista(request,artista_id):

#     artistas = Artista.objects.all()
#     return render(request, 'albumes.html', {'artistas':artistas})
