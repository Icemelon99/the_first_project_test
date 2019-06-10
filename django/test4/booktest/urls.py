from django.urls import path, include, re_path
from booktest import views

urlpatterns = [
	path('bookinfo/', views.book),
	path('create/', views.create),
	re_path(r'delete([0-9]+)', views.delete),
	path('test/', views.test),
	path('template/', views.template),
	path('pic_upload/', views.pic_upload),
	path('pic_handle/', views.pic_handle),
]