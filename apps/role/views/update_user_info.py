# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.role import models as mysql_db
from pubulic import public_methods


@csrf_exempt
def UserInfo(request):

    if request.method == 'POST':

        post = request.POST
        user_id = post["userId"]
        user_type = post["userType"]
        phone = post["phone"]
        sex = post["sex"]
        try:
            age = post["age"]
        except:
            age = ""
        name = post["name"]
        school = post["school"]

        # if user_type == "1":
        #     teach_type = post["teachType"]

        print public_methods.get_date_time(1, 1)

        person_table_update = mysql_db.Person.objects.get(user_id=user_id)
        person_table_update.update_time = public_methods.get_date_time(1, 1)

        if sex != "":
            person_table_update.sex = sex

        if phone != "":
            person_table_update.phone = phone

        if user_type == "0" or user_type == "1":

            teacher_table_update = mysql_db.Teacher.objects.get(user_id=user_id)

            if age != "":
                teacher_table_update.age = str(age)
            if school != "":
                teacher_table_update.school = school
            if name != "":
                teacher_table_update.name = name
            teacher_table_update.save()

        if user_type == 2:

            student_table_update = mysql_db.Student.objects.get(user_id=user_id)
            student_table_update.age = str(age)
            student_table_update.school = school
            student_table_update.save()

        person_table_update.save()

        response = {"message": "修改成功", "userId": user_id, "userType": user_type}

        if user_type == "0" or user_type == "1":

            return HttpResponse(public_methods.response_message("success", response, "100001"))

        elif user_type == "2":

            return HttpResponse(public_methods.response_message("success", response, "100002"))
