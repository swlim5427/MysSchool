# -*- coding: utf-8 -*-
# 教师课时详细列表查询
from __future__ import unicode_literals

from public import public_methods
from django.db.models import Count
from apps.class_manager import models as mysql_db
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def periods_list(request):

    if request.method == 'POST':

        post = request.POST

        teacher_id = post["teacherId"]

        if post["messageType"] == "list":

            if post["month"] == "13":

                m_s = public_methods.mkt_time(post["year"] + "-" + "1" + "-" + "1")
                m_e = public_methods.mkt_time(str(int(post["year"])+1) + "-" + "1" + "-" + "1")

            elif post["month"] == "0":
                m_s = public_methods.mkt_time(str(int(post["year"])-1) + "-" + "12" + "-" + "1")
                m_e = public_methods.mkt_time(post["year"] + "-" + "1" + "-" + "1")

            else:

                m_s = public_methods.mkt_time(post["year"] + "-" + post["month"] + "-" + "1")

                if post["month"] == "12":
                    m_e = public_methods.mkt_time(str(int(post["year"])+1) + "-" + "1" + "-" + "1")
                else:
                    m_e = public_methods.mkt_time(post["year"] + "-" + str(int(post["month"])+1) + "-" + "1")

            if post["selectType"] == "1":

                period_list = mysql_db.ClassPeriodStudent.objects.filter(
                        period_time__gte=m_s, period_time__lt=m_e
                ).filter(
                        teacher_id=teacher_id
                ).values(
                        'user_id', 'name'
                ).annotate(
                        periodCount=Count('user_id')
                ).order_by(
                        "user_id"
                )

            elif post["selectType"] == "0":

                period_list = mysql_db.ClassPeriodStudent.objects.filter(
                        period_time__gte=m_s, period_time__lt=m_e
                ).filter(
                        teacher_id=teacher_id
                ).values(
                        'user_id', 'name', 'period_data', 'period_time', 'class_time'
                ).order_by(
                        "period_time"
                )
            else:

                student_id = post["studentId"]

                period_list = mysql_db.ClassPeriodStudent.objects.filter(
                        period_time__gte=m_s, period_time__lt=m_e
                ).filter(
                        teacher_id=teacher_id, user_id=student_id
                ).values(
                        'teacher_id', 'class_teacher', 'user_id', 'name', 'period_data', 'period_time', 'class_time'
                ).order_by(
                        "period_time"
                )

            print period_list.query

            period_list = json.dumps(list(period_list))

            return HttpResponse(period_list)
