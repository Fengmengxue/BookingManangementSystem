# -*-coding:utf-8-*-
import random
from xml.etree.ElementTree import PI
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myadmin.models import User
from django.core.paginator import Paginator
# 封装或的条件搜索
from django.db.models import Q
from datetime import datetime
import hashlib, random


# 员工信息视图管理文件

def index(request, pIndex=1):
    '''view info'''
    umod = User.objects
    ulist = umod.filter(status__lt=9)
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get('keyword', None)
    if kw:
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        mywhere.append('keyword=' + kw)
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status" + status)
    # zhixing fenye chuli
    pIndex = int(pIndex)
    page = Paginator(ulist, 5)  # 以每页为五条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    elif pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息

    context = {"userlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/user/index.html", context)


def add(request):
    '''load info add form'''
    return render(request, "myadmin/user/add.html")


def insert(request):
    '''perform adding info'''
    try:
        ob = User()
        ob.username = request.POST["username"]
        ob.nickname = request.POST["nickname"]
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password'] + str(n)
        md5.update(s.encode('utf-8'))
        ob.password_hash = md5.hexdigest()
        ob.password_salt = n
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': 'insert successful'}
    except Exception as err:
        print(err)
        context = {'info': 'insert unccessful'}
    return render(request, "myadmin/info.html", context)


def delete(request, uid=0):
    '''delete info'''
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': 'delete successful'}
    except Exception as err:
        print(err)
        context = {'info': 'delete unccessful'}
    return render(request, "myadmin/info.html", context)


def edit(request, uid=0):
    '''load info edit form'''
    try:
        ob = User.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "myadmin/user/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': 'not find the info'}
    return render(request, "myadmin/info.html", context)


def update(request, uid=0):
    '''update info'''
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': 'update successful'}
    except Exception as err:
        print(err)
        context = {'info': 'update unccessful'}
    return render(request, "myadmin/info.html", context)
