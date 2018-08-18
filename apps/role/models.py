# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):

    # 用户表
    user_id = models.CharField('用户id',  max_length=255, unique=True)
    user_type = models.CharField('用户类型',  max_length=255, null=True)
    create_time = models.CharField('创建时间',  max_length=255, null=True)
    phone = models.CharField('电话号码',  max_length=255, null=True)
    password = models.CharField('密码',  max_length=255, null=True)
    status = models.CharField('状态（1：在职/在学，0：离职/退学）',  max_length=255, null=True)
    update_time = models.CharField('更新日期',  max_length=255, null=True)
    sex = models.CharField('性别（0：女，1：男)',  max_length=255, null=True)
    user_name = models.CharField('用户名（登陆名）',  max_length=255, null=True)

    def __unicode__(self):
        return self.user_id, self.user_type, \
               self.create_time, self.phone, \
               self.password, self.status, \
               self.update_time, self.sex, \
               self.user_name

    '''
    user_id：用户id
    user_type：用户类型（0：管理，1：老师，2：学员）
    create_time：创建时间
    phone：电话号码
    password：密码
    status：状态（1：在职/在学，0：离职/退学）
    update_time：更新日期
    sex：性别（0：女，1：男)
    user_name：用户名（登陆名）

    '''


class Teacher(models.Model):

    # 教师表
    # teacher = models.ForeignKey('Person', null=True)
    user_id = models.CharField('用户id',  max_length=255, unique=True)
    wx = models.CharField('微信',  max_length=255, null=True)
    teach_type = models.CharField('教师类型',  max_length=255, null=True)
    age = models.CharField('年龄',  max_length=255, null=True)
    salary = models.CharField('工资',  max_length=255, null=True)
    school = models.CharField('毕业学校',  max_length=255, null=True)
    level = models.CharField('教师级别 （1，2，3，4，5，6，7，8）',  max_length=255, null=True)
    entry_time = models.CharField('入职日期',  max_length=255, null=True)
    leave_time = models.CharField('离职日期',  max_length=255, null=True)
    name = models.CharField('姓名',  max_length=255, null=True)
    status = models.CharField('状态',  max_length=255, null=True)
    left_commit_periods = models.CharField('剩余待确认课时',  max_length=255, null=True)

    def __unicode__(self):
        return self.wx, self.teach_type, \
               self.age, self.salary, \
               self.school, self.entry_time, \
               self.leave_time, self.user_id, \
               self.level, self.name, \
               self.status

    '''
    user_id：用户id
    wx：微信
    teach_type：教师类型（200001：儿童美术，200002：水墨书法，200003：混合， 管理：0）
    age：年龄
    salary：工资
    school：毕业学校
    entry_time：入职日期
    leave_time：离职日期
    level：教师级别 （1，2，3，4，5，6，7，8）
    name：姓名
    status：状态（0 离职，1 在职）
    left_commit_periods：剩余待确认课时
    '''


class Student(models.Model):

    # 学员表
    # student = models.ForeignKey('Person', null=True)
    user_id = models.CharField('用户id', max_length=255, unique=True)
    wx = models.CharField('微信',  max_length=255, null=True)
    study_type = models.CharField('学员类型',  max_length=255, null=True)
    age = models.CharField('年龄',  max_length=255, null=True)
    price = models.CharField('学费',  max_length=255, null=True)
    periods = models.CharField('报名课时',  max_length=255, null=True)
    left_periods = models.CharField('剩余课时',  max_length=255, null=True)
    entry_time = models.CharField('报名日期',  max_length=255, null=True)
    leave_time = models.CharField('学完日期',  max_length=255, null=True)
    school = models.CharField('幼儿园/学校',  max_length=255, null=True)
    name = models.CharField('姓名',  max_length=255, null=True)
    status = models.CharField('状态',  max_length=255, null=True)
    contract_id = models.CharField('合同编号',  max_length=255, null=True)

    def __unicode__(self):
        return self.wx, self.study_type, \
               self.age, self.price, \
               self.periods, self.left_periods, \
               self.entry_time, self.leave_time, \
               self.user_id, self.school, \
               self.name, self.status, \
               self.contract_id

    '''
    user_id：用户id
    wx：微信
    study_type：学员类型（210001：儿童美术，210002：水墨，210003：混合）
    age：年龄
    price：学费
    periods：报名课时
    left_periods：剩余课时
    entry_time：报名日期
    leave_time：学完日期
    school：幼儿园/学校
    name：姓名
    birthday：生日
    status：状态（0 未在读，1 在读）
    contract_id：合同编号
    '''