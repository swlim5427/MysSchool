# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from apps.role import models as mysql_db
import json
import time


@csrf_exempt
def user_list(request):

    if request.method == 'POST':

        post = request.POST

        user_type = post["userType"]

        time.sleep(0.01)

        if user_type == "1":

            get_teacher_list = mysql_db.Teacher.objects.filter(status="1").filter(teach_type="1").values(
                    "name", "user_id", "age")
            teacher_list = json.dumps(list(get_teacher_list))
            return HttpResponse(teacher_list)

        elif user_type == "2":

            get_student_list = []
            
            try:
                terms = post["terms"]
            except:

                terms = "0"

            if terms == "0":

                get_student_list = mysql_db.Student.objects.filter(status="1").filter(left_periods__gt=0).values(
                        "name", "user_id", "age", "periods", "left_periods", "contract_id").order_by("contract_id")

            elif terms == "1":

                get_student_list = mysql_db.Student.objects.filter(status="1").values(
                        "name", "user_id", "age", "periods", "left_periods", "contract_id").order_by("contract_id")

            elif terms == "2":

                get_student_list = mysql_db.Student.objects.filter(
                        status="1"
                ).filter(
                        left_periods__gt=0, left_periods__lt=4
                ).values(
                        "name", "user_id", "age", "periods", "left_periods", "contract_id").order_by("contract_id")

            student_list = json.dumps(list(get_student_list))
            print len(list(get_student_list))
            return HttpResponse(student_list)

        else:

            get_teacher_list = mysql_db.Teacher.objects.filter(status="1").filter(teach_type="1").values(
                    "name", "user_id", "age")

            get_student_list = mysql_db.Student.objects.filter(status="1").filter(left_periods__gt=0).values(
                    "name", "user_id", "age", "periods", "left_periods", "contract_id").order_by("contract_id")

            response = {
                        "teacherList": json.dumps(list(get_teacher_list)),
                        "studentList": json.dumps(list(get_student_list)),
                        }

            return JsonResponse(response)
