from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
	list_per_page = 10
	actions_on_top = False
	actions_on_bottom = True
	list_display = ['id', 'btitle', 'bpub_date', 'read_comment']

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ['hname', 'hbook']