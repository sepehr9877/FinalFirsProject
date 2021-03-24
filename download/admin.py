from django.contrib import admin
from .models import DownloadSong,DownloadDetail
class AdminDownload(admin.ModelAdmin):
    list_display = ['UserDownload','is_paid','get__time']
    list_filter = ['UserDownload']
    sortable_by = ['get__time']
    search_fields = ['UserDownload']
class AdminDownloadDetail(admin.ModelAdmin):
    list_display = ['get_user_name','get_image_download','get_time']
    list_filter = ['Download',"recnetlydownload"]
    sortable_by = ['recnetlydownload']
admin.site.register(DownloadSong,AdminDownload)
admin.site.register(DownloadDetail,AdminDownloadDetail)
# Register your models here.
