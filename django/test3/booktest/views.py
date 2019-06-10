from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from datetime import date
# Create your views here.
def index(request):
	content = {
	'rpath': request.path,
	'rmethod': request.method,
	'rencoding': request.encoding,
	'rGET': request.GET,
	'rPOST': request.POST,
	}
	return render(request, 'booktest/index.html', content)

def args(request, id2):
	return HttpResponse(id2)

def login(request):
	if request.session.has_key('islogin'):
		return redirect('/login/index/')
	else:
		if 'username' in request.COOKIES:
			username = request.COOKIES['username']
		else:
			username = ''
		return render(request, 'booktest/login.html', {'username': username})

def login_check(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	remember = request.POST.get('remember')
	if username == 'admin' and password == '123':
		if remember == 'on':
			response = redirect('/login/index/')
			response.set_cookie('username', username, max_age=100000)
			request.session['islogin'] = True
			return response
		else:
			return redirect('/login/index/')
	else:
		return redirect('/login/login/')

def login_ajax(request):
	return render(request, 'booktest/login_ajax.html')

def login_ajax_check(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	remember = request.POST.get('remember')
	print(username, password, remember)
	if username == 'admin' and password == '123':
		return JsonResponse({'res': 1})
	else:
		return JsonResponse({'res': 0})

def set_cookie(request):
	response = render(request, 'booktest/cookie.html')
	response.set_cookie('cookie_dict', 'cookiesssss', max_age=1000000)
	return response

def get_cookie(request):
	cookie_dict = request.COOKIES
	return render(request, 'booktest/cookie2.html', cookie_dict)

def set_session(request):
	request.session['username'] = 'admin'
	request.session['password'] = '321'
	request.session.set_expiry(0)
	return HttpResponse('设置session')

def get_session(request):
	username = request.session['username']
	password = request.session.get('password')
	aged = request.session.get('aged', '没有信息')
	return HttpResponse(username+password+aged)

