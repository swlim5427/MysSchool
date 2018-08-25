# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.class_manager import models as mysql_db
from apps.role import models as role_db
from public import public_methods
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
import datetime


@csrf_exempt
def teacher_class_eliminate(request):

    if request.method == 'POST':
        post = request.POST
        class_id = post["classId"]

        if post["messageType"] == "init":

            student_list_info = mysql_db.ClassRelationStudent.objects.filter(class_id=class_id, status=1).values(
                    "user_id", "name", "age")
            student_info = []

            for i in range(len(student_list_info)):

                student_id = student_list_info[i]["user_id"]
                student_name = student_list_info[i]["name"]
                left_period = role_db.Student.objects.filter(user_id=student_id).values("left_periods")

                student_info.append({
                    "userId": student_id,
                    "name": student_name,
                    "leftPeriod": left_period[0]["left_periods"]
                })

            response = {"studentInfo": student_info}

            return JsonResponse(response)

        if post["messageType"] == "commit":

            print post
            # print post["studentLeftPeriod"]
            # print post["classInfo"]

            for i in range(len(eval(post["studentLeftPeriod"]))):

                if eval(post["studentLeftPeriod"])[i]["leftPeriod"] == "0":
                    response = {"message": "消课失败", "user": eval(post["studentLeftPeriod"])[i]["name"]}
                    result = "false"
                    result_code = "0"

                    return JsonResponse(public_methods.response_message(result, response, result_code))

            class_id = eval(post["classInfo"])["class_id"]
            student_list = eval(post["studentLeftPeriod"])
            class_name = eval(post["classInfo"])["class_name"]
            teacher_id = eval(post["classInfo"])["teacher_id"]
            teacher_name = eval(post["classInfo"])["teacher_name"]
            status = 0
            # period_time = int(time.time())
            # period_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            period_time = int(time.mktime(time.strptime(post["periodDate"], '%Y-%m-%d')))
            period_data = post["periodDate"]
            class_time = eval(post["classInfo"])["class_start_time"] + " - " + eval(post["classInfo"])["class_end_time"]
            class_week = public_methods.week(eval(post["classInfo"])["class_week"])
            class_time_info = class_week + "：" + class_time
            student_name_list = []

            for i in range(len(student_list)):
                student_name_list.append(student_list[i]["name"])

            class_period_teacher_self_add = mysql_db.ClassPeriodTeacherSelf(
                class_id=class_id,
                class_name=class_name,
                user_id=teacher_id,
                name=teacher_name,
                status=status,
                class_time=class_time_info,
                period_time=period_time,
                period_data=period_data,
                class_student=json.dumps(student_name_list),
            )
            class_period_teacher_self_add.save()

            response = {"message": "成功"}
            result = "success"
            result_code = "1"

            teacher_table_update = role_db.Teacher.objects.get(user_id=teacher_id)
            teacher_table_update.left_commit_periods = int(teacher_table_update.left_commit_periods) + 1
            teacher_table_update.save()

            return JsonResponse(public_methods.response_message(result, response, result_code))
