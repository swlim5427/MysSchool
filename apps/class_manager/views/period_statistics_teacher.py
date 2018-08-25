# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from public import public_methods
from django.db.models import Count
from apps.class_manager import models as mysql_db
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def period_statistics_teacher(request):

    if request.method == 'POST':

        post = request.POST

        teacher_id = post["teacherId"]

        if post["messageType"] == "list":

            if post["month"] == "13":

                m_s = public_methods.mkt_time(post["year"] + "-" + "1" + "-" + "1")
                m_e = public_methods.mkt_time(str(int(post["year"])+1) + "-" + "1" + "-" + "1")

            else:

                m_s = public_methods.mkt_time(post["year"] + "-" + post["month"] + "-" + "1")

                if post["month"] == "12":
                    m_e = public_methods.mkt_time(str(int(post["year"])+1) + "-" + "1" + "-" + "1")
                else:
                    m_e = public_methods.mkt_time(post["year"] + "-" + str(int(post["month"])+1) + "-" + "1")

            period_count = mysql_db.ClassPeriodStudent.objects.filter(
                    period_time__gt=m_s, period_time__lt=m_e
            ).filter(
                    teacher_id=teacher_id
            ).values(
                    'teacher_id', "class_teacher"
            ).annotate(
                    periodCount=Count('user_id')
            ).order_by(
                    "teacher_id"
            )

            print period_count.query

            teacher_list = json.dumps(list(period_count))

            return HttpResponse(teacher_list)
