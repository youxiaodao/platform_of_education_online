#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 22:10
# @Author  : DollA
# @File    : course.py
# @Software: PyCharm
# @Theme   :做序列化的类，都放在这里
from rest_framework import serializers

from luffyCity import models


# 2、创建类来序列化
class CourseSerializer(serializers.ModelSerializer):
    """
    课程序列化
    """
    level = serializers.CharField(source="get_level_display")
    class Meta:
        model = models.CourseList
        # fields = '__all__'
        # 13、将level也变成中文
        fields = ['id','title','course_img','level']


# 7、创建课程详细序列化类
class CourseDetailSerializer(serializers.ModelSerializer):
    """
    课程详细序列化
    """
    # 10、自定义字段，source处理 one2one/fk/choice 完全没问题，无法处理M2M
    title = serializers.CharField(source='course.title')
    img = serializers.CharField(source='course.course_img')
    # 11、要显示级别
    level = serializers.CharField(source='course.get_level_display')
    # 12、拿到推荐课程
    # 遇到M2M这样写，不会序列化，只会显示queryset
    recommends = serializers.CharField(source='recommend_courses.all')
    # m2m 除了depth，还可以
    recommends_2 = serializers.SerializerMethodField()
    # 14、显示章节
    chapter = serializers.SerializerMethodField()
    class Meta:
        model = models.CourseDetail
        # fields = '__all__'
        # 8、在详细页显示课程名,或者添加自定义字段
        # depth = 1
        # 只给想看到的
        # fields = ['slogon','why_learn']
        # 或者
        fields = ['chapter','recommends_2','recommends','course', 'title', 'img','level', 'slogon', 'why_learn']
        depth = 1

    def get_recommends_2(self,obj):
        # 获取推荐的所有课程
        queryset = obj.recommend_courses.all()
        return [{'id':row.id,'title':row.title} for row in queryset]

    def get_chapter(self,obj):
        """

        :param obj: 课程详细的对象
        :return:
        """
        # 反向查找，表名小写_set
        queryset = obj.course.chapter_set.all()
        return [{'id':row.id,'title':row.name} for row in queryset]