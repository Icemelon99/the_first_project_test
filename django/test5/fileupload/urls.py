from django.urls import path, include, re_path
from fileupload import views

urlpatterns = [
	path('upload/', views.upload),
	path('handle/', views.handle),
	path('editor/', views.editor),
	path('submit/', views.submit),
	path('session_set/', views.session_set),
	path('session_get/', views.session_get),
	path('set_get/', views.set_get),
	path('paste/', views.paste),
	path('celery_test/', views.celery_test),
	path('test1/', views.test1),
]
