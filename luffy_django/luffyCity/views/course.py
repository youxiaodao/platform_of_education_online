#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 11:13
# @Author  : Doll
# @File    : course.py
# @Software: PyCharm
# @Theme   :
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from luffyCity import models
from luffyCity.auth.auth import LuffyAuth

# 2、创建类来序列化
# class CourseSerializer(my_serializers.ModelSerializer):
#     level = my_serializers.CharField(source="get_level_display")
#     class Meta:
#         model = models.CourseList
#         # fields = '__all__'
#         # 13、将level也变成中文
#         fields = ['id','title','course_img','level']
#
#
# # 7、创建课程详细序列化类
# class CourseDetailSerializer(my_serializers.ModelSerializer):
#     # 10、自定义字段，source处理 one2one/fk/choice 完全没问题，无法处理M2M
#     title = my_serializers.CharField(source='course.title')
#     img = my_serializers.CharField(source='course.course_img')
#     # 11、要显示级别
#     level = my_serializers.CharField(source='course.get_level_display')
#     # 12、拿到推荐课程
#     # 遇到M2M这样写，不会序列化，只会显示queryset
#     recommends = my_serializers.CharField(source='recommend_courses.all')
#     # m2m 除了depth，还可以
#     recommends_2 = my_serializers.SerializerMethodField()
#     # 14、显示章节
#     chapter = my_serializers.SerializerMethodField()
#     class Meta:
#         model = models.CourseDetail
#         # fields = '__all__'
#         # 8、在详细页显示课程名,或者添加自定义字段
#         # depth = 1
#         # 只给想看到的
#         # fields = ['slogon','why_learn']
#         # 或者
#         fields = ['chapter','recommends_2','recommends','course', 'title', 'img','level', 'slogon', 'why_learn']
#         depth = 1
#
#     def get_recommends_2(self,obj):
#         # 获取推荐的所有课程
#         queryset = obj.recommend_courses.all()
#         return [{'id':row.id,'title':row.title} for row in queryset]
#
#     def get_chapter(self,obj):
#         """
#
#         :param obj: 课程详细的对象
#         :return:
#         """
#         # 反向查找，表名小写_set
#         queryset = obj.course.chapter_set.all()
#         return [{'id':row.id,'title':row.name} for row in queryset]

# 5、as_view要加参数来区分不同的请求，要换一个as_view
from rest_framework.viewsets import GenericViewSet, ViewSetMixin

from luffyCity.my_serializers import course


class Course(ViewSetMixin, APIView):
    # def get(self, request, *args, **kwargs):
    # ret = {
    #     'code':1000,
    #     'data':[
    #         {'id':1,'title':'python全栈'},
    #         {'id':2,'title':'Linux运维'},
    #         {'id':3,'title':'金融分析'}
    #     ]
    # }
    # from json import JSONEncoder
    #
    # ret = {'code': 1000, 'data': None}
    # try:
    #     # 1、拿到querySet,json不能序列化queryset，要用serializer
    #     courseQueryset = models.CourseList.objects.all()
    #     # 3、实例化serializer
    #     ser = CourseSerializer(instance=courseQueryset, many=True)
    #     # 4、返回状态
    #     ret['data'] = ser.data
    # except Exception as e:
    #     ret['code'] = 1001
    #     ret['error'] = '获取课程失败'
    #
    # return Response(ret)

    def list(self, request, *args, **kwargs):
        """
        课程列表的接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            # 1、拿到querySet,json不能序列化queryset，要用serializer
            courseQueryset = models.CourseList.objects.all()
            # 3、实例化serializer
            ser = course.CourseSerializer(instance=courseQueryset, many=True)
            # 4、返回状态
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retreive(self, request, *args, **kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            # obj = models.CourseList.objects.filter(pk=pk).first()
            # 6、应该用课程详细表,查询到课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=pk).first()
            # 用CourseDetailSerializer
            ser = course.CourseDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data

        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)


class MicroView(APIView):
    authentication_classes = [LuffyAuth]

    def get(self, request, *args, **kwargs):
        # token = request.query_params.get('token')
        # obj = models.UserToken.objects.filter(token=token)
        # if not obj:
        #     return Response('认证失败')
        print(request.user)
        print(request.auth)
        ret = {'code': 1000, 'title': '微职位'}
        return Response(ret)
