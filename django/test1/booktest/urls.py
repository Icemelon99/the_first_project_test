from django.urls import path, re_path, include
from booktest import views

urlpatterns = [
	path('index', views.index),
	path('', views.books),
	re_path(r'([0-9]+)', views.detail)
]