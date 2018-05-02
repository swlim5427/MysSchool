# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.role import models as mysql_db
from pubulic import public_methods


@csrf_exempt
def user_info(request):

    if request.method == 'POST':

        message = {}

        post = request.POST
        user_id = post["userId"]
        user_type = post["userType"]
        message_type = post["messageType"]

        get_user_info = mysql_db.Person.objects.get(user_id=user_id)

        if message_type == "loginSearch":

            if user_type == "0" or user_type == "1":

                get_teacher_info = mysql_db.Teacher.objects.get(user_id=user_id)

                phone = get_user_info.phone
                status = get_user_info.status
                sex = get_user_info.sex
                teach_type = get_teacher_info.teach_type
                age = get_teacher_info.age
                salary = get_teacher_info.salary
                school = get_teacher_info.school
                level = get_teacher_info.level
                name = get_teacher_info.name

                message = {"phone": phone,
                           "sex": sex,
                           "teachType": teach_type,
                           "age": age,
                           "school": school,
                           "name": name
                           }

            elif user_type == "2":

                get_student_info = mysql_db.Student.objects.get(user_id=user_id)
                phone = get_user_info.phone
                status = get_user_info.status
                sex = get_user_info.sex
                study_type = get_student_info.study_type
                age = get_student_info.age
                price = get_student_info.price
                school = get_student_info.school
                periods = get_student_info.periods
                left_periods = get_student_info.left_periods
                name = get_student_info.name

                message = {"phone": phone,
                           "status": status,
                           "sex": sex,
                           "age": age,
                           "school": school,
                           "name": name,
                           "studyType": study_type,
                           "periods": periods,
                           "leftPeriods": left_periods
                           }
            message.setdefault('userId', user_id)
            message.setdefault('userType', user_type)

        response_message = {"message": message}
        response = public_methods.response_message("success", response_message, "100001")
        return JsonResponse(response)



        # get_user_info((user_id, user_type))


# def get_user_info(message):
#
#     user_id = message[0]
#     user_type = message[1]
#
#     if user_type == "0" or user_type == "1":
#
#         get_user = mysql_db.Person.objects.get(user_id=user_id)
#         user_id1 = get_user.user_id
#         get_teacher = mysql_db.Teacher.objects.get(user_id=user_id)
#
#         user_type1 = get_teacher.teach_type
#
#         response_message = {"message": "登陆成功", "userId": user_id, "userType": user_type}
#
#         response = public_methods.response_message("success", response_message, "100001")
#
#         return JsonResponse(response)
