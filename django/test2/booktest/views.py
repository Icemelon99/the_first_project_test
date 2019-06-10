from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from booktest.models import HeroInfo
# Create your views here.

def login_required(func):
    """登录状态验证装饰器"""
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('islogin'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/main/login/')
    return wrapper

@login_required
def main(request):
    """登录后显示的主页"""
    return render(request, 'booktest/main.html')


def login(request, a, *args):
    """登录页面"""
    return render(request, 'booktest/login.html')


def login_check(request):
    """登录判断"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    varifycode = request.POST.get('varifycode')
    if username == 'admin' and password == '123' and varifycode == request.session['verifycode']:
        request.session['islogin'] = True
        return redirect('/main/')
    else:
        return redirect('/main/login/')




@login_required
def personal_msg(request):
    return HttpResponse('这是个人信息页面')

@login_required
def change_psw(request):
    return HttpResponse('这是修改密码页面')

@login_required
def logout(request):
    request.session.flush()
    return HttpResponse('退出登录')

# 完成生成验证码功能
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
import random
def varify_code(request):
    bgcolor = (random.randrange(20, 200),
               random.randrange(20, 200),
               255)
    width = 100
    height = 25
    im = Image.new('RGB', (width, height), bgcolor)
    draw = ImageDraw.Draw(im)
    for i in range(0, 200):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    str1 = 'abcd123efghijk45lmn6opqrst789uvwxyz0'
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    font = ImageFont.truetype('FreeMono.ttf', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    for i in range(4):
        draw.text(((25*i + 5), random.randrange(-3,3)), rand_str[i], font=font, fill=fontcolor)
    del draw
    request.session['verifycode'] = rand_str
    buf = BytesIO()
    im.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')

def url_test(request):
    return redirect(reverse('booktest:login', args=('as',)))


def page_display(request, pindex):
    heros = HeroInfo.objects.all()
    p = Paginator(heros, 5)
    if pindex == '':
        pindex = 1
    heros = p.page(int(pindex))
    plist = p.page_range
    comment = {'heros': heros, 'plist': plist}
    return render(request, 'booktest/page_display.html', comment)