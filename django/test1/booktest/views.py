from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo, HeroInfo
# Create your views here.

def index_test(request):
	# 1. 加载模板文件，模板对象(其中模板路径从templates目录下计起)
	temp = loader.get_template('booktest/index.html')
	# 2. 定义模板上下文，给模板传递数据，第二个参数为传递数据用字典
	context = RequestContext(request, {})
	# 3. 模板渲染，产生标准的html内容(在django2.x下context必须是字典)
	res_html = temp.render(context)
	return HttpResponse(res_html)

def index(request):
	return render(request, 'booktest/index.html', {'name':'这是一个views内容测试', 
	'list': range(10) })

def hello(request):
	return HttpResponse('这是一个URL正则测试')

def books(request):
	'''显示图书的信息'''
	books = BookInfo.objects.all()
	content = {'books': books}
	return render(request, 'booktest/books.html', content)

def detail(request, bid):
	'''根据ID查询图书'''
	book = BookInfo.objects.get(id=bid)
	heros = book.heroinfo_set.all()
	content = {
		'bookname': book.btitle, 
		'heros': heros
	}
	return render(request, 'booktest/detail.html', content)



