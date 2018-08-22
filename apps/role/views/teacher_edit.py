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
def teacher_edit(request):
    now_time = int(time.time())
    if request.method == 'POST':
        post = request.POST

        teacher_id = post["teacherId"]

        message_type = post["messageType"]

        if message_type == "init":

            person_search = mysql_db.Person.objects.filter(user_id=teacher_id).values(
                    "phone", "sex")
            teacher_search = mysql_db.Teacher.objects.filter(user_id=teacher_id).values(
                    "age", "salary", "school", "name", "level")

            person_info = json.dumps(list(person_search)[0])

            teacher_info = json.dumps(list(teacher_search)[0])

            response = {"personInfo": person_info, "teacherInfo": teacher_info}

            return JsonResponse(response)

        if message_type == "edit":
            print "1"
            user_id = post["teacherId"]
            name = post["teacherName"]
            phone = post["teacherPhone"]
            update_time = now_time
            sex = post["teacherSex"]
            salary = post["teacherSalary"]
            level = post["teacherLevel"]
            school = post["teacherSchool"]

            update_person = mysql_db.Person.objects.get(user_id=user_id)
            update_person.phone = phone
            update_person.sex = sex
            update_person.update_time = update_time

            update_teacher = mysql_db.Teacher.objects.get(user_id=user_id)
            update_teacher.name = name
            update_teacher.salary = salary
            update_teacher.level = level
            update_teacher.school = school

            try:
                update_person.save()
                update_teacher.save()

                response = {"message": "更新成功", "user_id": user_id}
                result = "success"
                result_code = "1"

            except Exception as e:
                print e
                response = {"message": "更新失败", "user_id": user_id}
                result = "false"
                result_code = "0"

            return JsonResponse(public_methods.response_message(result, response, result_code))
