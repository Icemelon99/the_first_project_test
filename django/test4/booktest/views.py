from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from booktest.models import BookInfo, HeroInfo, PicTest
from django.urls import reverse
from datetime import date
from django.conf import settings
from django.core.paginator import Paginator
# Create your views here.

def book(request):
	books = BookInfo.objects.all()
	content = {'books': books}
	return render(request, 'booktest/book.html', content)

def create(request):
	b = BookInfo()
	b.btitle = '流星蝴蝶剑'
	b.bpub_date = date(1990, 1, 1)
	b.save()
	# return HttpResponseRedirect('/index/bookinfo/')
	# return HttpResponse('OK')
	# return render(request, 'x.html', content)
	# return redirect(reverse(views方法))
	return redirect('/index/bookinfo/')

def delete(request, bid):
	b = BookInfo.objects.get(id=bid)
	b.delete()
	return redirect('/index/bookinfo/')

def test(request):
	test1 = 1
	test2 = [1, 2, 3, 4]
	test3 = {'a': 'aa', "b": 'bb'}
	content = {
		'test1': test1,
		'test2': test2,
		'test3': test3,
	}
	return render(request, 'booktest/test.html', content)

def template(request):
	content = {'content': '<h1>content</h1>'}
	return render(request, 'booktest/template.html', content)

def pic_upload(request):
	return render(request, 'booktest/pic_upload.html')

def pic_handle(request):
	pict = request.FILES.get('pic')
	pic_dir = '{}/booktest/{}'.format(settings.MEDIA_ROOT, pict.name)
	with open(pic_dir, 'wb') as f:
		for line in pict.chunks():
			f.write(line)
	PicTest.objects.create(pic='booktest/{}'.format(pict.name))
	return HttpResponse('OK')

def page_display(request):
	pass