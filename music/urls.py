from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^artistas/$', views.artistas, name='artistas'),
    # url(r'^artista/(?P<artista_id>\d+)/albumes/$', views.albumes_por_artista, name='albumes_por_artista'),
    # url(r'^artista/album/(?P<album_id>\d+)/$', views.tracks_por_album, name='tracks_por_album'),
]