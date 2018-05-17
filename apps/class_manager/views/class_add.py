# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.curriculum import models as mysql_db
from pubulic import public_methods
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
        student_id = post["student_id"]
        class_start_time = post["classStartTime"]
        class_time = post["classTime"]
        class_end_time = post["classEndTime"]
        class_id = ""

        try:
            class_id = mysql_db.Curriculum.objects.order_by('-class_id')[0].curriculum_id
            class_id = int(class_id) + 1
        except:
            curriculum_id = "1100001"

        add_curriculum = mysql_db.Curriculum(
            class_name=class_name,
            curriculum_id=curriculum_id,
            class_id=class_id,
            teacher_id=teacher_id,
            class_start_time=class_start_time,
            class_time=class_time,
            class_end_time=class_end_time,
            student_id=student_id,
            status="1"
        )
        try:
            add_curriculum.save()
            response = {"message": "班级创建成功", "class_id": class_id}
            result = "success"
            result_code = "1"

        except Exception as e:
            print e
            # if e[0] == 1062:
            #     curriculum_status = mysql_db.Curriculum.objects.get(curriculum_name=curriculum_name).status
            #
            #     if curriculum_status == "1":
            #         response = {"message": "课程名重复"}
            #         result = "false"
            #         result_code = "0"
            #     else:
            #
            #         curriculum_status_update = mysql_db.Curriculum.objects.get(curriculum_name=curriculum_name)
            #         curriculum_status_update.status = "1"
            #         curriculum_status_update.save()

            response = {"message": "班级创建失败", "class_id": class_id}
            result = "false"
            result_code = "0"

        return JsonResponse(public_methods.response_message(result, response, result_code))
