# @Author : 会吃饭的小刘
# @Python 3.9
# @Time : 2022/5/13 16:44
# @Email : xautliuzhengzheng@163.com
# coding = utf-8
from django.urls import path
from. import views

urlpatterns = [
    path('', views.login_view)
]
