# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Assortment(models.Model):

    # 课程-分类
    assortment_id = models.CharField('分类id', max_length=255, unique=True)
    assortment_name = models.CharField('分类名', max_length=255, unique=True)

    def __unicode__(self):
        return self.assortment_id, self.assortment_name

    '''
    assortment_id：分类id
    assortment_name：分类名
    '''



class Curriculum(models.Model):

    # 课程-字典表
    curriculum_id = models.CharField('课程id', max_length=255, unique=True)
    curriculum_name = models.CharField('课程名',  max_length=255, null=True)
    assortment_id = models.CharField('课程分类id',  max_length=255, null=True)

    def __unicode__(self):
        return self.curriculum_id, self.curriculum_name, self.assortment_id

    '''
    curriculum_id：课程id
    curriculum_name：课程名
    assortment_id：课程分类id
    '''


class ClassRelation(models.Model):
    # 班级-自定义班级列表
    curriculum_id = models.CharField('课程id', max_length=255, unique=True)
    curriculum_teacher = models.CharField('任课老师', max_length=255, unique=True)
    curriculum_name = models.CharField('班级名称', max_length=255, unique=True)
    curriculum_student = models.CharField('上课学生', max_length=255, unique=True)
    curriculum_time = models.CharField('上课时间', max_length=255, unique=True)
    curriculum_date = models.CharField('上课日期', max_length=255, unique=True)
    curriculum_week = models.CharField('上课日期', max_length=255, unique=True)

    def __unicode__(self):
        return self.curriculum_id, self.curriculum_teacher, \
               self.curriculum_name, self.curriculum_student, \
               self.curriculum_time, self.curriculum_date, \
               self.curriculum_week
    '''
    curriculum_id：课程id
    curriculum_teacher：任课老师
    curriculum_name：班级名称
    curriculum_student：上课学生
    curriculum_time：上课时间
    curriculum_date：上课日期
    curriculum_week：上课日期
    '''