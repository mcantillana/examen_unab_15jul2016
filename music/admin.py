from django.contrib import admin
from music.models import Artista, Album, Track


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre','orden','created_at','updated_at')
    # list_filter = ('owner','active')
    # list_search = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nombre','ano','orden','artista','created_at','updated_at')
    list_filter = ('artista','ano')
    list_search = ('nombre',)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('nombre','duracion_min','duracion_seg','numero','album','created_at','updated_at')
    list_filter = ('album',)
    list_search = ('nombre',)


admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
