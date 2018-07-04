# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.class_manager import models as mysql_db
from public import public_methods
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def class_add(request):

    if request.method == 'POST':
        post = request.POST

        class_name = post["className"]
        # 课程信息
        curriculum_info = json.loads(post["curriculumInfo"])
        curriculum_name = curriculum_info["curriculum_name"]
        curriculum_id = curriculum_info["curriculum_id"]
        # 教师信息
        teacher_info = json.loads(post["teacherInfo"])
        teacher_name = teacher_info["name"]
        teacher_id = teacher_info["user_id"]

        # 学生信息
        student_list = eval(post["studentInfo"])
        student_name_list = []

        if student_list != "":

            for i in range(len(student_list)):
                student_name_list.append(student_list[i]["name"])

        class_start_time = post["startTime"]
        class_time = ""
        class_end_time = post["endTime"]
        class_week = post["week"]
        assortment_type = post["assortmentType"]

        try:
            class_id = mysql_db.ClassInfo.objects.order_by('-class_id')[0].class_id
            class_id = int(class_id) + 1

        except:
            class_id = "1100001"

        add_class = mysql_db.ClassInfo(
            class_name=class_name,
            curriculum_name=curriculum_name,
            curriculum_id=curriculum_id,
            class_id=class_id,
            teacher_id=teacher_id,
            teacher_name=teacher_name,
            class_start_time=class_start_time,
            class_time=class_time,
            class_end_time=class_end_time,
            class_student=json.dumps(student_name_list),
            class_week=class_week,
            assortment_type=assortment_type,
            status="1"
        )

        for i in range(len(student_list)):

            add_class_relation_student = mysql_db.ClassRelationStudent(
                class_id=class_id,
                class_name=class_name,
                user_id=student_list[i]["user_id"],
                name=student_list[i]["name"],
                age=student_list[i]["age"],
                periods=student_list[i]["periods"],
                left_periods=student_list[i]["left_periods"],
                status="1"
            )
            add_class_relation_student.save()

        add_class_relation_teacher = mysql_db.ClassRelationTeacher(
            class_id=class_id,
            class_name=class_name,
            user_id=teacher_id,
            name=teacher_name,
            status="1"
        )
        add_class_relation_teacher.save()

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
