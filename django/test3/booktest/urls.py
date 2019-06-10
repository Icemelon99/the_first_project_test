from django.urls import path, include, re_path
from booktest import views

urlpatterns = [
	path('index/', views.index),
	re_path(r'args(?P<id2>\d+)/', views.args),
	path('login/', views.login),
	path('login_check/', views.login_check),
	path('login_ajax/', views.login_ajax),
	path('login_ajax_check/', views.login_ajax_check),
	path('set_cookie/', views.set_cookie),
	path('get_cookie/', views.get_cookie),
	path('set_session/', views.set_session),
	path('get_session/', views.get_session),
]