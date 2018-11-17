#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 23:37
# @Author  : DollA
# @File    : auth.py
# @Software: PyCharm
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from luffyCity import models

class LuffyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.UserToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({'code':1001,'error':'认证失败'})
        return (obj.user.user,obj)