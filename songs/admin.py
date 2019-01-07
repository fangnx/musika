from django.contrib import admin

# Register your models here.
from .models import Song

class SongModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'artist', 'added_time', 'updated_time']
    list_filter = ['added_time', 'updated_time']
    search_fields = ['title', 'artist']
    class Meta:
        model = Song

admin.site.register(Song, SongModelAdmin)
