# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.class_manager import models as mysql_db
from public import public_methods
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def class_add(request):

    if request.method == 'POST':
        post = request.POST

        curriculum_id = post["curriculumId"]
        class_name = post["className"]
        teacher_id = post["teacherId"]
        student_id_list = post["student_id"]
        class_start_time = post["classStartTime"]
        class_time = post["classTime"]
        class_end_time = post["classEndTime"]
        class_week = post["class_week"]

        try:
            class_id = mysql_db.ClassInfo.objects.order_by('-class_id')[0].class_id
            class_id = int(class_id) + 1

        except:
            class_id = "1100001"

        add_class = mysql_db.ClassInfo(
            class_name=class_name,
            curriculum_id=curriculum_id,
            class_id=class_id,
            teacher_id=teacher_id,
            class_start_time=class_start_time,
            class_time=class_time,
            class_end_time=class_end_time,
            student_id=student_id_list,
            class_week=class_week,
            status="1"
        )

        for student_id in student_id_list:

            add_class_relation = mysql_db.ClassRelation(
                class_id=class_id,
                teacher_id=teacher_id,
                student_id=student_id
            )

            add_class_relation.save()

        try:
            add_class.save()
            response = {"message": "班级创建成功", "class_id": class_id}
            result = "success"
            result_code = "1"

        except Exception as e:
            print e

            response = {"message": "班级创建失败", "class_id": class_id}
            result = "false"
            result_code = "0"

        return JsonResponse(public_methods.response_message(result, response, result_code))
