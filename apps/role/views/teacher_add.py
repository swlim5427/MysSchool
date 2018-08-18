# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.role import models as mysql_db
from public import public_methods
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time


@csrf_exempt
def teacher_add(request):
    now_time = int(time.time())
    if request.method == 'POST':
        post = request.POST

        try:
            l_user_id = mysql_db.Teacher.objects.order_by('-user_id')[0].user_id
            user_id = int(l_user_id) + 1

        except:
            user_id = "10000001"

        user_type = 1

        name = post["teacherName"]
        phone = post["teacherPhone"]
        create_time = now_time
        sex = post["teacherSex"]
        # age = post["teacherAge"]
        age = 100
        salary = post["teacherSalary"]
        school = post["teacherSchool"]
        entry_time = now_time
        status = 1
        user_name = phone
        pass_word = 123456
        teach_type = 1
        level = post["teacherLevel"]

        insert_person = mysql_db.Person(
                user_id=user_id,
                user_type=user_type,
                create_time=str(create_time),
                phone=phone,
                password=pass_word,
                status=status,
                sex=sex,
                user_name=user_name
        )

        insert_teacher = mysql_db.Teacher(
                teach_type=teach_type,
                age=age,
                salary=salary,
                entry_time=entry_time,
                school=school,
                name=name,
                user_id=user_id,
                status=status,
                level=level,
                left_commit_periods=0
        )

        try:
            insert_person.save()
            insert_teacher.save()
            response = {"message": "成功"}
            result = "success"
            result_code = "1"

        except Exception as e:
            print e
            response = {"message": "失败"}
            result = "false"
            result_code = "0"

        return JsonResponse(public_methods.response_message(result, response, result_code))
