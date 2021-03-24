from django.contrib import admin
from .models import Comments,User_Comments,Subscriber,Blogs
class AdminSubscriber(admin.ModelAdmin):
    list_display = ('image_tag','username','email')
    search_fields = ['username','email']
    sortable_by = ['username']
    list_filter = ['username']
class AdminUserComments(admin.ModelAdmin):
    list_display = ['__str__','get_image_user','get_time_of_comment']
    search_fields = ['__str__']
    list_filter = ['comments']
admin.site.register(Comments)
admin.site.register(Blogs)
admin.site.register(Subscriber)
admin.site.register(User_Comments)
# Register your models here.
