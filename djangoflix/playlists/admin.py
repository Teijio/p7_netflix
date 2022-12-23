from django.contrib import admin

from .models import Playlist, PlaylistItem


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0 # исправляет отображение в админке


@admin.register(Playlist)
class PlaylistItemAdmin(admin.ModelAdmin):
    inlines = [ PlaylistItemInline ]
    class Meta:
        model = Playlist
