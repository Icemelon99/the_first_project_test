from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, PicTest
# Register your models here.

class BookTabularInline(admin.TabularInline):
	model = HeroInfo
	extra = 2

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
	list_per_page = 10
	actions_on_top = False
	actions_on_bottom = True
	list_display = ['id', 'btitle', 
	'bpub_date', 'read_comment', 'book_person']
	list_filter = ['btitle', 'bpub_date']
	search_fields = ['btitle', 'id']
	# fields = ['bpub_date', 'btitle']
	fieldsets = (
		('基本', {'fields': ['btitle', 'bpub_date']}),
		('高级', {'fields': ['bread', 'bcomment']}),
		)
	inlines = [BookTabularInline]



@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ['hname', 'hbook']


@admin.register(PicTest)
class PicAdmin(admin.ModelAdmin):
	pass
