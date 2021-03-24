from django.contrib import admin
from .models import FavoritMusic,FavoritDetail
class AdminFavoritMusic(admin.ModelAdmin):
    list_display = ['FavoritUser','TimeFavorti']
    list_filter = ['TimeFavorti','FavoritUser']

admin.site.register(FavoritMusic,AdminFavoritMusic)
admin.site.register(FavoritDetail)
# Register your models here.
