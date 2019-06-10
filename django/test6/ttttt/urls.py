from django.urls import path, re_path, include
from ttttt import views

urlpatterns = [
	path('index/', views.index),
]
