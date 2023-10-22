from django.contrib import admin
from myadmin.models import Notice
# Register your models here.
admin.site.site_header='Notice hub'
admin.site.index_title='Admin panel'


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id' ,'subject','description','created_at','updated_at']
admin.site.register(Notice,NoticeAdmin)