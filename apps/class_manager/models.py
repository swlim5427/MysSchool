# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ClassInfo(models.Model):
    # 班级-自定义班级列表
    class_id = models.CharField('班级id', max_length=255, unique=True, null=True)
    curriculum_id = models.CharField('课程id', max_length=255, null=True)
    class_teacher = models.CharField('任课老师', max_length=255, null=True)
    class_name = models.CharField('班级名称', max_length=255, null=True)
    class_student = models.CharField('上课学生', max_length=255, null=True)
    class_start_time = models.CharField('上课开始时间', max_length=255, null=True)
    class_time = models.CharField('上课时间', max_length=255, null=True)
    class_end_time = models.CharField('下课时间', max_length=255, null=True)
    class_week = models.CharField('上课日期星期', max_length=255, null=True)
    status = models.CharField('状态',  max_length=255, null=True)

    def __unicode__(self):
        return self.class_id, self.class_teacher, \
               self.class_name, self.class_student, \
               self.class_start_time, self.class_time, \
               self.class_end_time, self.class_week, \
               self.curriculum_id, self.status

    '''
    class_id：班级id
    curriculum_id：课程id
    class_teacher：任课老师
    class_name：班级名称
    class_student：上课学生(列表)
    class_time：上课时间
    class_start_time：上课开始时间
    class_end_time：下课时间s
    class_week：上课日期星期
    status：课程状态（0 失效，1 生效）

    '''


class ClassRelation(models.Model):
    # 班级-班级关系
    class_id = models.CharField('班级id', max_length=255, unique=True, null=True)
    teacher_id = models.CharField('任课老师', max_length=255, null=True)
    student_id = models.CharField('上课学生', max_length=255, null=True)

    def __unicode__(self):
        return self.class_id, self.teacher_id, \
               self.student_id

    '''
    class_id：课程id
    class_teacher：任课老师
    class_name：班级名称
    class_student：上课学生
    class_time：上课时间
    class_date：上课日期
    class_week：上课日期

    '''