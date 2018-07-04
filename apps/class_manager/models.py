# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ClassInfo(models.Model):
    # 班级-自定义班级列表
    class_id = models.CharField('班级id', max_length=255, unique=True, null=True)
    curriculum_name = models.CharField('课程名', max_length=255, null=True)
    curriculum_id = models.CharField('课程id', max_length=255, null=True)
    teacher_id = models.CharField('任课老师id', max_length=255, null=True)
    teacher_name = models.CharField('任课老师', max_length=255, null=True)
    class_name = models.CharField('班级名称', max_length=255, null=True)
    class_student = models.CharField('上课学生', max_length=255, null=True)
    class_start_time = models.CharField('上课开始时间', max_length=255, null=True)
    class_time = models.CharField('上课时间', max_length=255, null=True)
    class_end_time = models.CharField('下课时间', max_length=255, null=True)
    class_week = models.CharField('上课日期星期', max_length=255, null=True)
    assortment_type = models.CharField('课程分类', max_length=255, null=True)
    status = models.CharField('状态',  max_length=255, null=True)

    def __unicode__(self):
        return self.class_id, self.teacher_name, \
               self.class_name, self.class_student, \
               self.class_start_time, self.class_time, \
               self.class_end_time, self.class_week, \
               self.curriculum_id, self.status, \
               self.assortment_type, self.curriculum_name

    '''
    class_id：班级id
    curriculum_name：课程名
    curriculum_id：课程名
    teacher_id：任课老师id
    teacher_name：任课老师
    class_name：班级名称
    class_student：上课学生(列表)
    class_time：上课时间
    class_start_time：上课开始时间
    class_end_time：下课时间s
    class_week：上课日期星期
    assortment_type：课程分类
    status：课程状态（0 失效，1 生效）

    '''


class ClassRelationTeacher(models.Model):
    # 班级-班级关系-教师
    class_id = models.CharField('班级id', max_length=255, unique=True, null=True)
    class_name = models.CharField('班级名称', max_length=255, null=True)
    user_id = models.CharField('任课老师id', max_length=255, null=True)
    name = models.CharField('任课老师姓名', max_length=255, null=True)
    status = models.CharField('状态', max_length=255, null=True)

    def __unicode__(self):
        return self.class_id, self.teacher_id, \
               self.class_name, self.teacher_name, \
               self.status

    '''
    class_id：课程id
    class_name：班级名称
    teacher_id：任课老师id
    teacher_name：任课老师姓名
    status：教师状态（0 离职，1 在职）
    '''


class ClassRelationStudent(models.Model):
    # 班级-班级关系-学生
    class_id = models.CharField('班级id', max_length=255, null=True)
    class_name = models.CharField('班级名称', max_length=255, null=True)
    user_id = models.CharField('学生id', max_length=255, null=True)
    name = models.CharField('学生姓名', max_length=255, null=True)
    status = models.CharField('状态', max_length=255, null=True)
    age = models.CharField('年龄', max_length=255, null=True)
    periods = models.CharField('课时', max_length=255, null=True)
    left_periods = models.CharField('剩余课时', max_length=255, null=True)

    def __unicode__(self):
        return self.class_id, self.student_id, \
               self.class_name, self.student_name, \
               self.status, self.age, \
               self.periods, self.left_periods

    '''
    class_id：课程id
    class_name：班级名称
    student_id：任课老师id
    student_name：任课老师姓名
    status：学生状态（0 未在学，1 在学）
    periods：总课时
    left_periods：剩余课时
    '''
