from django.db import models


# Create your models here.


class CourseList(models.Model):
    title = models.CharField(max_length=32, verbose_name='课程名')
    course_img = models.CharField(max_length=32, verbose_name='课程图片',null=True)
    course_level = (
        (1, '初级'),
        (2, '中级'),
        (3, '高级')
    )
    level = models.IntegerField(verbose_name='课程等级', choices=course_level, default=1)

    def __str__(self):
        return self.title


class CourseDetail(models.Model):
    course = models.OneToOneField(to='CourseList', on_delete=True)
    slogon = models.CharField(verbose_name='口号', max_length=255,null=True)
    why_learn = models.CharField(verbose_name='为什么要学这门课', max_length=255,null=True)
    recommend_courses = models.ManyToManyField(verbose_name='推荐课程', to='CourseList', related_name='rc')

    def __str__(self):
        return "课程详细:%s" % self.course.title


class Chapter(models.Model):
    course = models.ForeignKey(to='CourseList', on_delete=True)
    name = models.CharField(verbose_name='章节名称', max_length=32)
    num = models.IntegerField(verbose_name='章节')

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo',on_delete=True)
    token = models.CharField(max_length=64)
# 可以加超时时间
