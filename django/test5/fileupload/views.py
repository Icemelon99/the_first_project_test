from django.shortcuts import render, redirect, HttpResponse
from fileupload.models import FileTest, GoodInfo
from django.conf import settings
from .tasks import add_test
# Create your views here.

def upload(request):
	return render(request, 'fileupload/upload.html')

def handle(request):
	file = request.FILES.get('file')
	file_dir = '{}/fileupload/{}'.format(settings.MEDIA_ROOT, file.name)
	with open(file_dir, 'wb') as f:
		for i in file.chunks():
			f.write(i)
	FileTest.objects.create(file='fileupload/{}'.format(file.name))
	return HttpResponse('OK')

def editor(request):
	return render(request, 'fileupload/editor.html')

def submit(request):
	comment = request.POST.get('gcomment')
	print(comment, type(comment))
	GoodInfo.objects.create(gcontent=comment)
	return HttpResponse('OK')

def session_set(request):
	request.session['name'] = '1111111om'
	request.session['age'] = '1219'
	return HttpResponse('设置session')

def session_get(request):
	name = request.session['name']
	age = request.session['age']
	return HttpResponse(name+age)

def set_get(request):
	a = request.GET['a']
	b = request.GET.get('b')
	return HttpResponse(a+b)

def paste(request):
	text = request.POST.get('textarea')
	print(text)
	return HttpResponse(text)

def celery_test(request):
	text = add_test.delay() # 返回的不是add_test的return，而是一个task的唯一id，其存储在redis中，是一个<class 'celery.result.AsyncResult'>对象
	print(type(text))
	return HttpResponse(text)

def test1(request):
	return render(request, 'test1.html')