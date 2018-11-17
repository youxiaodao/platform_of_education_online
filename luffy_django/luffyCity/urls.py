#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 11:10
# @Author  : DollA
# @File    : urls.py
# @Software: PyCharm
# @Theme   :
# from django.urls import re_path
from django.conf.urls import url
from luffyCity.views import course,account
urlpatterns = [
    # 方式一，判断是否穿进去PK值，只要pk有值，就是单条数据
    # url(r'^course',course.Course.as_view()),
    # url(r'^course/(?P<id>\d+)$',course.Course.as_view()),
    # 方式二，
    url(r'^course/$',course.Course.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)$',course.Course.as_view({'get':'retreive'})),
    url(r'^login/$',account.LoginView.as_view()),
    url(r'^micro',course.MicroView.as_view())

]
