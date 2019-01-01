# -*- coding: utf-8 -*-
# 学生课时详细列表查询
from __future__ import unicode_literals

from public import public_methods
from django.db.models import Count
from apps.class_manager import models as mysql_db
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def student_periods_list(request):

    if request.method == 'POST':

        post = request.POST

        student_id = post["studentId"]

        if post["messageType"] == "list":

            if post["selectType"] == "0":

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

                period_list = mysql_db.ClassPeriodStudent.objects.filter(
                        period_time__gte=m_s, period_time__lt=m_e
                ).filter(
                        user_id=student_id
                ).values(
                        'user_id', 'name', 'period_data', 'period_time', 'class_time', 'class_teacher'
                ).order_by(
                        "period_time"
                    )
            else:

                period_list = mysql_db.ClassPeriodStudent.objects.filter(
                        user_id=student_id
                ).values(
                        'user_id', 'name', 'period_data', 'period_time', 'class_time', 'class_teacher'
                ).order_by(
                        "period_time"
                )

            print period_list.query

            period_list = json.dumps(list(period_list))

            return HttpResponse(period_list)
