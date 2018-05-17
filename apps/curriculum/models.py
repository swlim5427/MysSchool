# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Assortment(models.Model):

    # 课程-分类
    assortment_id = models.CharField('分类id', max_length=255, unique=True, null=True)
    assortment_name = models.CharField('分类名', max_length=255, unique=True, null=True)

    def __unicode__(self):
        return self.assortment_id, self.assortment_name

    '''
    assortment_id：分类id
    assortment_name：分类名
    '''


class Curriculum(models.Model):

    # 课程-字典表
    curriculum_id = models.CharField('课程id', max_length=255, unique=True, null=True)
    curriculum_name = models.CharField('课程名',  max_length=255, unique=True, null=True)
    assortment_id = models.CharField('课程分类id',  max_length=255, null=True)
    status = models.CharField('状态',  max_length=255, null=True)

    def __unicode__(self):
        return self.curriculum_id, self.curriculum_name, self.assortment_id

    '''
    curriculum_id：课程id
    curriculum_name：课程名
    assortment_id：课程分类id
    status：课程状态（0 失效，1 生效）
    '''