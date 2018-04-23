# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.role import models as mysql_db
from apps.role.views import public_methods


@csrf_exempt
class UserInfo:

    def __init__(self, request):

        if request.method == 'POST':

            self.post = request.POST
            self.user_id = self.post["userId"]
            self.user_type = self.post["userType"]
            self.phone = self.post["phone"]
            self.sex = self.post["sex"]
            self.age = self.post["age"]
            self.school = self.post["school"]

            if self.user_type == "1":
                self.teach_type = self.param["teachType"]

            self.update_user_info()

    def update_user_info(self):

        person_table_update = mysql_db.Person.objects.get(user_id=self.user_id)
        person_table_update.update_time = public_methods.get_date_time(1, 1)
        person_table_update.sex = self.sex
        person_table_update.phone = self.phone

        if self.user_type == 1:

            teacher_table_update = mysql_db.Teacher.objects.get(user_id=self.user_id)
            teacher_table_update.age = str(self.age)
            teacher_table_update.school = self.school
            teacher_table_update.save()

        if self.user_type == 2:

            student_table_update = mysql_db.Student.objects.get(user_id=self.user_id)
            student_table_update.age = str(self.age)
            student_table_update.school = self.school
            student_table_update.save()

        person_table_update.save()

        response = {"message": "修改成功", "userId": self.user_id, "userType": self.user_type}

        if self.user_type == "1":

            return HttpResponse(public_methods.response_message("success", response, "100001"))

        elif self.user_type == "2":

            return HttpResponse(public_methods.response_message("success", response, "100002"))
