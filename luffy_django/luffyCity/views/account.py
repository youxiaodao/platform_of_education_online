#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 19:56
# @Author  : DollA
# @File    : account.py
# @Software: PyCharm
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse

from luffyCity import models


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        # obj = HttpResponse('')
        # obj['Access-Control-Allow-Origin'] = '*'
        ret = {'code': 1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')

        user_obj = models.UserInfo.objects.filter(user=user, pwd=pwd).first()
        if user_obj:
            import uuid
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user_obj, defaults={'token': uid})
            ret['token'] = uid
        else:
            ret['code'] = 1001
            ret['error'] = '用户名或者密码错误'

        return Response(ret)


"""
    def options(self, request, *args, **kwargs):
        print(request.data)
        # obj = HttpResponse('')
        # obj['Access-Control-Allow-Headers'] = 'Content-type'
        # obj['Access-Control-Allow-Origin'] = '*'

        return Response('...')
"""
