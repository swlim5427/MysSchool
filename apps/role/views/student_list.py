# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from apps.role import models as mysql_db
from django.db.models import Q
import json
import time


@csrf_exempt
def student_list(request):

    if request.method == 'POST':

        post = request.POST

        user_name = post["name"]
        s_student_list = eval(post["selectStudentList"])

        if user_name == "undefined":
            user_name = ""

        select_student_list = []

        for i in range(6):
            try:
                select_student = s_student_list[i]
            except:
                select_student = {"user_id": "1"}

            select_student_list.append(select_student)

        get_student_list = mysql_db.Student.objects.filter(
                ~Q(user_id=select_student_list[0]["user_id"]),
                ~Q(user_id=select_student_list[1]["user_id"]),
                ~Q(user_id=select_student_list[2]["user_id"]),
                ~Q(user_id=select_student_list[3]["user_id"]),
                ~Q(user_id=select_student_list[4]["user_id"]),
                ~Q(user_id=select_student_list[5]["user_id"])
        ).filter(name__contains=user_name, status=1).values(
                "user_id", "name", "age", "periods", "left_periods", "contract_id"
        ).filter(left_periods__gt=0
                 ).order_by("contract_id")

        print get_student_list

        student_list_r = json.dumps(list(get_student_list))
        return HttpResponse(student_list_r)
