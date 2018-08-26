# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.class_manager import models as mysql_db
from apps.role import models as role_db
from public import public_methods
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json


@csrf_exempt
def class_edit(request):

    if request.method == 'POST':
        post = request.POST
        class_id = post["classId"]

        if post["messageType"] == "init":

            class_info = mysql_db.ClassInfo.objects.filter(class_id=class_id, status=1).values(
                    "class_name", "class_start_time", "class_end_time", "curriculum_id", "curriculum_name")

            teacher_info = mysql_db.ClassRelationTeacher.objects.filter(class_id=class_id, status=1).values(
                    "user_id", "name")

            student_list_info = mysql_db.ClassRelationStudent.objects.filter(class_id=class_id, status=1).values(
                    "user_id", "name", "age", "periods", "left_periods")

            teacher_info = json.dumps(teacher_info[0])
            class_info = json.dumps(class_info[0])

            select_student_list = []

            for i in range(6):
                try:
                    select_student = student_list_info[i]
                except:
                    select_student = {"user_id": "1"}

                select_student_list.append(select_student)

            left_student_list = role_db.Student.objects.filter(
                    ~Q(user_id=select_student_list[0]["user_id"]),
                    ~Q(user_id=select_student_list[1]["user_id"]),
                    ~Q(user_id=select_student_list[2]["user_id"]),
                    ~Q(user_id=select_student_list[3]["user_id"]),
                    ~Q(user_id=select_student_list[4]["user_id"]),
                    ~Q(user_id=select_student_list[5]["user_id"])
            ).filter(status=1).filter(left_periods__gt=0
                 ).values("user_id", "name", "age", "periods", "left_periods")

            for i in range(len(select_student_list)):
                try:
                    select_student_list[i]["name"]
                except:
                    del select_student_list[i:]

            response = {"classInfo": class_info,
                        "teacherInfo": teacher_info,
                        "selectStudentList": json.dumps(list(select_student_list)),
                        "lefStudentList": json.dumps(list(left_student_list))
                        }

            return JsonResponse(response)

        if post["messageType"] == "edit":

            print class_id

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
            # class_week = post["week"]
            # assortment_type = post["assortmentType"]

            update_class = mysql_db.ClassInfo.objects.get(class_id=class_id)

            update_class.class_name = class_name
            update_class.curriculum_name = curriculum_name
            update_class.curriculum_id = curriculum_id
            update_class.teacher_id = teacher_id
            update_class.teacher_name = teacher_name
            update_class.class_start_time = class_start_time
            update_class.class_time = class_time
            update_class.class_end_time = class_end_time
            update_class.class_student = json.dumps(student_name_list)

            update_class_relation_teacher = mysql_db.ClassRelationTeacher.objects.get(class_id=class_id)
            update_class_relation_teacher.class_name = class_name
            update_class_relation_teacher.user_id = teacher_id
            update_class_relation_teacher.name = teacher_name
            # 需要改造成 json
            mysql_db.ClassRelationStudent.objects.filter(class_id=class_id).delete()

            try:
                update_class_relation_teacher.save()
                update_class.save()

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

                response = {"message": "班级更新成功", "class_id": class_id}
                result = "success"
                result_code = "1"

            except Exception as e:
                print e
                response = {"message": "班级更新失败", "class_id": class_id}
                result = "false"
                result_code = "0"

            return JsonResponse(public_methods.response_message(result, response, result_code))
