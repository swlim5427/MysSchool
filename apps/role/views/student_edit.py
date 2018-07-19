# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.role import models as mysql_db
from public import public_methods
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
import json


@csrf_exempt
def student_edit(request):
    now_time = int(time.time())
    if request.method == 'POST':
        post = request.POST

        student_id = post["studentId"]

        message_type = post["messageType"]

        if message_type == "init":

            person_search = mysql_db.Person.objects.filter(user_id=student_id).values(
                    "phone", "sex")
            student_search = mysql_db.Student.objects.filter(user_id=student_id).values(
                    "age", "price", "periods", "school", "name")

            person_info = json.dumps(list(person_search)[0])

            student_info = json.dumps(list(student_search)[0])

            response = {"personInfo": person_info, "studentInfo": student_info}

            return JsonResponse(response)

        if message_type == "edit":

            user_id = post["studentId"]
            name = post["studentName"]
            phone = post["studentPhone"]
            update_time = now_time
            sex = post["studentSex"]
            age = post["studentAge"]
            price = post["studentPrice"]
            # periods = post["studentPeriods"]
            # left_periods = post["studentPeriods"]
            school = post["studentSchool"]

            update_persion = mysql_db.Person.objects.get(user_id=user_id)
            update_persion.phone = phone
            update_persion.sex = sex
            update_persion.update_time = update_time

            update_student = mysql_db.Student.objects.get(user_id=user_id)
            update_student.age = age
            update_student.name = name
            update_student.price = price
            # update_student.periods = periods
            update_student.school = school

            try:
                update_persion.save()
                update_student.save()

                response = {"message": "更新成功", "user_id": user_id}
                result = "success"
                result_code = "1"

            except Exception as e:
                print e
                response = {"message": "更新失败", "user_id": user_id}
                result = "false"
                result_code = "0"

            return JsonResponse(public_methods.response_message(result, response, result_code))

        if message_type == "addPeriods":
            user_id = post["studentId"]
            add_periods = int(post["addPeriods"])

            update_student_periods = mysql_db.Student.objects.get(user_id=user_id)
            update_student_periods.periods = int(update_student_periods.periods) + add_periods
            update_student_periods.left_periods = int(update_student_periods.left_periods) + add_periods

            try:
                update_student_periods.save()

                response = {"message": "更新成功", "user_id": user_id}
                result = "success"
                result_code = "1"

            except Exception as e:
                print e
                response = {"message": "更新失败", "user_id": user_id}
                result = "false"
                result_code = "0"

            return JsonResponse(public_methods.response_message(result, response, result_code))
