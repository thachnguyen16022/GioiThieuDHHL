from django.contrib import admin
from .models import giamhieu,comments
# Register your models here.
class giamhieuAdmin(admin.ModelAdmin):
    list_display=('giamhieu_id','name','chuc_vu','sdt','email','nhiem_vu','anh')
    search_fields=['name']
    list_filter=('giamhieu_id','name','chuc_vu','sdt','email','nhiem_vu')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('cmt_id', 'cmt', 'ho_ten')
    search_fields = ['ho_ten']
    list_filter = ('cmt_id', 'ho_ten')
    
admin.site.register(giamhieu,giamhieuAdmin)
admin.site.register(comments, CommentsAdmin)
