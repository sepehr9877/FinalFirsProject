
from django.contrib import admin
from .models import Album
# admin.site.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    sortable_by = 'Year'
    list_filter = ["Year",]
    list_display = ('image_tag','AlbumName','Year',)
    search_fields = ('AlbumName','Year')
# Register your models here.
admin.site.register(Album,AlbumAdmin)
