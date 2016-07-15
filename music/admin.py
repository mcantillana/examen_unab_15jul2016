from django.contrib import admin
from music.models import Artista


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre','orden','created_at','updated_at')
    # list_filter = ('owner','active')
    # list_search = ('name',)

admin.site.register(Artista, ArtistaAdmin)
