from django.contrib import admin
from fileupload.models import FileTest, GoodInfo
# Register your models here.

@admin.register(FileTest)
class FileAdmin(admin.ModelAdmin):
	list_display = ['id', 'file']

@admin.register(GoodInfo)
class GoodAdmin(admin.ModelAdmin):
	list_display = ['id']