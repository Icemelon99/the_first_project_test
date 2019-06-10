from django.urls import path, re_path
from booktest import views

urlpatterns=[
	re_path(r'login/([asd]+)/', views.login, name='login'),
	path('login_check/', views.login_check),
	path('', views.main),
	path('personal_msg/', views.personal_msg),
	path('change_psw/', views.change_psw),
	path('varify_code/', views.varify_code),
	path('logout/', views.logout),
	path('url_test/', views.url_test),
	re_path('page_display(?P<pindex>[0-9]*)/', views.page_display),
]