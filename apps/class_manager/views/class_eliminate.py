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
def class_eliminate(request):

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
            print post["studentLeftPeriod"]
            print post["classInfo"]

            for i in range(len(eval(post["studentLeftPeriod"]))):

                if eval(post["studentLeftPeriod"])[i]["leftPeriod"] == "0":
                    response = {"message": "消课失败", "user": eval(post["studentLeftPeriod"])[i]["name"]}
                    result = "false"
                    result_code = "0"

                    return JsonResponse(public_methods.response_message(result, response, result_code))

            student_list = eval(post["studentLeftPeriod"])
            class_id = eval(post["classInfo"])["class_id"]
            class_name = eval(post["classInfo"])["class_name"]
            teacher_id = eval(post["classInfo"])["teacher_id"]
            teacher_name = eval(post["classInfo"])["teacher_name"]
            status = 1
            period_time = int(time.time())
            period_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            class_time = eval(post["classInfo"])["class_start_time"] + " - " + eval(post["classInfo"])["class_end_time"]
            class_week = public_methods.week(eval(post["classInfo"])["class_week"])
            class_time_info = class_week + "：" + class_time
            student_name_list = []

            for i in range(len(student_list)):
                student_name_list.append(student_list[i]["name"])
                class_period_student_add = mysql_db.ClassPeriodStudent(
                    class_id=class_id,
                    class_name=class_name,
                    user_id=student_list[i]["userId"],
                    name=student_list[i]["name"],
                    status=1,
                    period_time=period_time,
                    period_data=period_data,
                    class_time=class_time_info,
                    class_teacher=teacher_name
                )
                class_period_student_add.save()
                update_student_period = role_db.Student.objects.get(user_id=student_list[i]["userId"])
                update_student_period.left_periods = int(update_student_period.left_periods) - 1
                update_student_period.save()

            class_period_teacher_add = mysql_db.ClassPeriodTeacher(
                class_id=class_id,
                class_name=class_name,
                user_id=teacher_id,
                name=teacher_name,
                status=status,
                period_data=period_data,
                period_time=period_time,
                class_time=class_time_info,
                class_student=student_name_list
            )
            class_period_teacher_add.save()

            response = {"message": "成功"}
            result = "success"
            result_code = "1"

            return JsonResponse(public_methods.response_message(result, response, result_code))

        if post["messageType"] == "teacherCommit":

            print post
            print post["studentLeftPeriod"]
            print eval(post["classInfo"])["id"]

            for i in range(len(eval(post["studentLeftPeriod"]))):

                if eval(post["studentLeftPeriod"])[i]["leftPeriod"] == "0":
                    response = {"message": "消课失败", "user": eval(post["studentLeftPeriod"])[i]["name"]}
                    result = "false"
                    result_code = "0"

                    return JsonResponse(public_methods.response_message(result, response, result_code))

            student_list = eval(post["studentLeftPeriod"])
            class_id = eval(post["classInfo"])["class_id"]
            class_name = eval(post["classInfo"])["class_name"]
            teacher_id = eval(post["classInfo"])["teacher_id"]
            teacher_name = eval(post["classInfo"])["teacher_name"]
            status = 1
            period_time = int(time.time())
            period_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            class_time = eval(post["classInfo"])["class_start_time"] + " - " + eval(post["classInfo"])["class_end_time"]
            class_week = public_methods.week(eval(post["classInfo"])["class_week"])
            class_time_info = class_week + "：" + class_time
            student_name_list = []

            for i in range(len(student_list)):
                student_name_list.append(student_list[i]["name"])
                class_period_student_add = mysql_db.ClassPeriodStudent(
                    class_id=class_id,
                    class_name=class_name,
                    user_id=student_list[i]["userId"],
                    name=student_list[i]["name"],
                    status=1,
                    period_time=period_time,
                    period_data=period_data,
                    class_time=class_time_info,
                    class_teacher=teacher_name
                )
                # class_period_student_add.save()
                update_student_period = role_db.Student.objects.get(user_id=student_list[i]["userId"])
                update_student_period.left_periods = int(update_student_period.left_periods) - 1
                # update_student_period.save()

            class_period_teacher_add = mysql_db.ClassPeriodTeacher(
                class_id=class_id,
                class_name=class_name,
                user_id=teacher_id,
                name=teacher_name,
                status=status,
                period_data=period_data,
                period_time=period_time,
                class_time=class_time_info,
                class_student=student_name_list
            )
            # class_period_teacher_add.save()

            response = {"message": "成功"}
            result = "success"
            result_code = "1"

            return JsonResponse(public_methods.response_message(result, response, result_code))
