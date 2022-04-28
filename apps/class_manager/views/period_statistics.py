# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from public import public_methods
from django.db.models import Count, Sum
from apps.class_manager import models as mysql_db
from apps.role import models as role_db
# from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def period_statistics(request):

    if request.method == 'POST':

        post = request.POST

        print post

        if post["messageType"] == "list":
            year = "2021"
            post["year"] = year
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

            # period_count = mysql_db.ClassPeriodTeacher.objects.filter(period_time__gt=m_s, period_time__lt=m_e).
            # values(
            #         'user_id',
            #         'name',
            # ).annotate(
            #         periodCount=Count('user_id')
            # ).order_by(
            #         "status",
            #         "user_id"
            # )

            period_count = mysql_db.ClassPeriodStudent.objects.filter(period_time__gte=m_s, period_time__lt=m_e).values(
                    'teacher_id',
                    'class_teacher'
            ).annotate(
                    periodCount=Count('teacher_id')
            ).order_by(
                    'teacher_id'
            )

            teacher_list = json.dumps(list(period_count))

            return HttpResponse(teacher_list)

        if post["messageType"] == "indexPeriodsList":

            print post["messageType"]

            print post["year"]

            period_list = []

            for i in range(1, 13):

                m_s = public_methods.mkt_time(post["year"] + "-" + str(i) + "-" + "1")

                if i == 12:
                    m_e = public_methods.mkt_time(str(int(post["year"])+1) + "-" + "1" + "-" + "1")
                else:
                    m_e = public_methods.mkt_time(post["year"] + "-" + str(i+1) + "-" + "1")

                period_count = mysql_db.ClassPeriodStudent.objects.filter(
                        period_time__gte=m_s,
                        period_time__lt=m_e).count()

                period_list.append(period_count)

            period_month = return_function(period_list)
            return HttpResponse(period_month)

        if post["messageType"] == "periodIncomeList":

            print post["messageType"]

            print post["year"]

            period_income_list = []

            for i in range(1, 13):

                m_s = public_methods.mkt_time(post["year"] + "-" + str(i) + "-" + "1")

                if i == 12:
                    m_e = public_methods.mkt_time(str(int(post["year"])+1) + "-" + "1" + "-" + "1")
                else:
                    m_e = public_methods.mkt_time(post["year"] + "-" + str(i+1) + "-" + "1")

                period_income = mysql_db.ClassPeriodStudent.objects.filter(
                        period_time__gte=m_s,
                        period_time__lt=m_e
                ).values(
                        'price_period'
                ).aggregate(
                        period_income=Sum('price_period')
                )

                print period_income

                if period_income["period_income"] == None:
                    period_income["period_income"] = 0

                period_income_list.append(period_income["period_income"])

            period_month = return_function(period_income_list)
            return HttpResponse(period_month)

        if post["messageType"] == "sellIncomeList":

            print post["messageType"]

            print post["year"]

            sell_income_list = []

            for i in range(1, 13):

                m_s = public_methods.mkt_time(post["year"] + "-" + str(i) + "-" + "1")

                if i == 12:
                    m_e = public_methods.mkt_time(str(int(post["year"])+1) + "-" + "1" + "-" + "1")
                else:
                    m_e = public_methods.mkt_time(post["year"] + "-" + str(i+1) + "-" + "1")

                sell_income = role_db.Student.objects.filter(
                        entry_time__gte=m_s,
                        entry_time__lt=m_e
                ).filter(
                        status=1
                ).values(
                        'price'
                ).aggregate(
                        sell_income=Sum('price')
                )

                print sell_income

                if sell_income["sell_income"] == None:
                    sell_income["sell_income"] = 0

                sell_income_list.append(sell_income["sell_income"])

            period_month = return_function(sell_income_list)
            return HttpResponse(period_month)


def return_function(period_list):

    period_month = {
        "Jan": 0,
        "Feb": 0,
        "Mar": 0,
        "Apr": 0,
        "May": 0,
        "June": 0,
        "July": 0,
        "Aug": 0,
        "Sept": 0,
        "Oct": 0,
        "Nov": 0,
        "Dec": 0
    }

    period_month.update({
        "Jan": period_list[0],
        "Feb": period_list[1],
        "Mar": period_list[2],
        "Apr": period_list[3],
        "May": period_list[4],
        "June": period_list[5],
        "July": period_list[6],
        "Aug": period_list[7],
        "Sept": period_list[8],
        "Oct": period_list[9],
        "Nov": period_list[10],
        "Dec": period_list[11]
    })

    print period_month

    period_month = json.dumps(period_month)

    return period_month
