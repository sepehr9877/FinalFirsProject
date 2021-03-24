from django.contrib import admin
from .models import Artist
class ArtistAdmin(admin.ModelAdmin):
    sortable_by = "ArtistName"
    list_display = ('image_tag','ArtistName')
    search_fields = ['ArtistName',]
    list_filter = ['ArtistName']
    list_editable = ['ArtistName']

admin.site.register(Artist,ArtistAdmin)
# Register your models here.
