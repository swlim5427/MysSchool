# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-17 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0003_auto_20180417_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='create_time',
            field=models.CharField(max_length=255, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=255, null=True, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=255, null=True, verbose_name='\u7535\u8bdd\u53f7\u7801'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6027\u522b\uff080\uff1a\u5973\uff0c1\uff1a\u7537)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(max_length=255, null=True, verbose_name='\u72b6\u6001\uff081\uff1a\u5728\u804c/\u5728\u5b66\uff0c0\uff1a\u79bb\u804c/\u9000\u5b66\uff09'),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_time',
            field=models.CharField(max_length=255, null=True, verbose_name='\u66f4\u65b0\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_id',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u7528\u6237id'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_name',
            field=models.CharField(max_length=255, null=True, verbose_name='\u7528\u6237\u540d\uff08\u767b\u9646\u540d\uff09'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_type',
            field=models.CharField(max_length=255, null=True, verbose_name='\u7528\u6237\u7c7b\u578b\uff080\uff1a\u7ba1\u7406\uff0c1\uff1a\u8001\u5e08\uff0c2\uff1a\u5b66\u5458\uff09'),
        ),
    ]
