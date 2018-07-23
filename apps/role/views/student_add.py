# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.role import models as mysql_db
from public import public_methods
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time


@csrf_exempt
def student_add(request):
    now_time = int(time.time())
    if request.method == 'POST':
        post = request.POST

        try:
            l_user_id = mysql_db.Student.objects.order_by('-user_id')[0].user_id
            user_id = int(l_user_id) + 1

        except:
            user_id = "20000001"

        user_type = 2

        contract_id = post["contractId"]
        name = post["studentName"]
        phone = post["studentPhone"]
        creat_time = now_time
        sex = post["studentSex"]
        age = post["studentAge"]
        price = post["studentPrice"]
        periods = post["studentPeriods"]
        left_periods = post["studentPeriods"]
        school = post["studentSchool"]
        entry_time = now_time
        status = 1
        user_name = user_id
        pass_word = user_id
        study_type = 210003

        insert_persion = mysql_db.Person(
                user_id=user_id,
                user_type=user_type,
                create_time=str(creat_time),
                phone=phone,
                password=pass_word,
                status=status,
                sex=sex,
                user_name=user_name
        )

        insert_student = mysql_db.Student(
                study_type=study_type,
                age=age,
                price=price,
                periods=periods,
                left_periods=left_periods,
                entry_time=entry_time,
                school=school,
                name=name,
                user_id=user_id,
                status=status,
                contract_id=contract_id
        )

        try:
            insert_persion.save()
            insert_student.save()
            response = {"message": "成功"}
            result = "success"
            result_code = "1"

        except Exception as e:
            print e
            response = {"message": "失败"}
            result = "false"
            result_code = "0"
        # insert_persion.save()
        # insert_student.save()
        # response = {"message": "成功"}
        # result = "success"
        # result_code = "1"

        return JsonResponse(public_methods.response_message(result, response, result_code))
