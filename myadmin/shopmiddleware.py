# -*-coding:utf-8-*-
from django.shortcuts import redirect
from django.urls import reverse
import re

# 中间件
class ShopMiddleware:
    def __init__(self, get_response):  # 初始化
        self.get_response = get_response
        # One-time configuration and initialization.
        print("ShopMiddleware")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = request.path
        print("url:", path)

        # 判断管理后台是否登录
        # 定义后台不登录页可直接访问的url列表
        urllist = ['/myadmin/login/','/myadmin/logout/', '/myadmin/dologin/', '/myadmin/verify/' ]
        # 判断当前请求 url 地址 是否是以 myadmin开头, and buzai urlistzhong, caizuodenglupanduan
        if re.match(r'^/myadmin/', path) and (path not in urllist):
            # 判断是否登录
            if 'adminuser' not in request.session:  #  后台的名字都会是adminuser
                # redirected to login page重定向到登录页
                return redirect(reverse("myadmin_login"))

        # 判断大堂点餐请求的判断，判断是否登录（session中是否有webuser）
        if re.match(r'^/web', path):
            # 判断是否登录(在于session中没有webuser)
            if 'webuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("web_login"))
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response