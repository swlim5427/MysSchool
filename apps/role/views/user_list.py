# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from apps.role import models as mysql_db
import json
import time


@csrf_exempt
def user_list(request):

    if request.method == 'POST':

        post = request.POST
    # if request.method == 'GET':
    #
    #     post = request.GET
        user_type = post["userType"]

        time.sleep(0.01)

        get_teacher_list = mysql_db.Teacher.objects.filter(status="1").values("name", "user_id")
        get_student_list = mysql_db.Student.objects.filter(status="1").values("name", "user_id")

        all_user_list = json.dumps(list(get_teacher_list.union(get_student_list)))
        teacher_list = json.dumps(list(get_teacher_list))
        student_list = json.dumps(list(get_student_list))

        if user_type == "1":

            return HttpResponse(teacher_list)

        elif user_type == "2":

            return HttpResponse(student_list)

        else:

            return HttpResponse(all_user_list)
