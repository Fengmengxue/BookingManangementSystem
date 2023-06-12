"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myadmin.views import index
from myadmin.views import user, shop, category, product, member

urlpatterns = [
    path('', index.index, name="myadmin_index"),  # houtai shouye
    # 后台管理员 login exit urls
    path('login/', index.login, name="myadmin_login"),
    path('dologin/', index.dologin, name="myadmin_dologin"),  # 执行登录
    path('logout/', index.logout, name="myadmin_logout"),
    path('verify/', index.verify, name="myadmin_verify"),
    # employee info management urls
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),  # view
    path('user/add', user.add, name="myadmin_user_add"),  # add form
    path('user/insert', user.insert, name="myadmin_user_insert"),  # perform add
    path('user/delete/<int:uid>', user.delete, name="myadmin_user_delete"),  # perform delete
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),  # load edit form
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # perform edit

    # shop info management urls
    path('shop/<int:pIndex>', shop.index, name="myadmin_shop_index"),  # view
    path('shop/add', shop.add, name="myadmin_shop_add"),  # add form
    path('shop/insert', shop.insert, name="myadmin_shop_insert"),  # perform add
    path('shop/delete/<int:sid>', shop.delete, name="myadmin_shop_delete"),  # perform delete
    path('shop/edit/<int:sid>', shop.edit, name="myadmin_shop_edit"),  # load edit form
    path('shop/update/<int:sid>', shop.update, name="myadmin_shop_update"),  # perform edit
    # 菜品类别信息管理路由
    path('category/<int:pIndex>', category.index, name="myadmin_category_index"),  # 浏览
    path('category/load/<int:sid>', category.loadCategory, name="myadmin_category_load"),
    path('category/add', category.add, name="myadmin_category_add"),  # 添加表单
    path('category/insert', category.insert, name="myadmin_category_insert"),  # 执行添加
    path('category/del/<int:cid>', category.delete, name="myadmin_category_del"),  # 执行删除
    path('category/edit/<int:cid>', category.edit, name="myadmin_category_edit"),  # 加载编辑表单
    path('category/update/<int:cid>', category.update, name="myadmin_category_update"),  # 执行编辑

    # 菜品信息管理路由
    path('product/<int:pIndex>', product.index, name="myadmin_product_index"),  # 浏览
    path('product/add', product.add, name="myadmin_product_add"),  # 添加表单
    path('product/insert', product.insert, name="myadmin_product_insert"),  # 执行添加
    path('product/del/<int:pid>', product.delete, name="myadmin_product_del"),  # 执行删除
    path('product/edit/<int:pid>', product.edit, name="myadmin_product_edit"),  # 加载编辑表单
    path('product/update/<int:pid>', product.update, name="myadmin_product_update"),  # 执行编辑
    # 会员信息管理路由
    path('member/<int:pIndex>', member.index, name="myadmin_member_index"),  # 浏览
]
