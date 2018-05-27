# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.curriculum import models as mysql_db
from public import public_methods
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def curriculum_add(request):

    if request.method == 'POST':
        post = request.POST

        curriculum_name = post["curriculumName"]
        assortment_id = post["assortmentId"]

        try:
            curriculum_id = mysql_db.Curriculum.objects.order_by('-curriculum_id')[0].curriculum_id
            curriculum_id = int(curriculum_id) + 1
        except:
            curriculum_id = "1100001"

        add_curriculum = mysql_db.Curriculum(
            curriculum_name=curriculum_name,
            assortment_id=assortment_id,
            curriculum_id=curriculum_id,
            status="1"
        )
        try:
            add_curriculum.save()
            response = {"message": "课程创建成功", "curriculumId": curriculum_id}
            result = "success"
            result_code = "1"

        except Exception as e:
            print e
            if e[0] == 1062:
                curriculum_status = mysql_db.Curriculum.objects.get(curriculum_name=curriculum_name).status

                if curriculum_status == "1":
                    response = {"message": "课程名重复"}
                    result = "false"
                    result_code = "0"
                else:

                    curriculum_status_update = mysql_db.Curriculum.objects.get(curriculum_name=curriculum_name)
                    curriculum_status_update.status = "1"
                    curriculum_status_update.save()

                    response = {"message": "课程创建成功", "curriculumId": curriculum_id}
                    result = "success"
                    result_code = "1"

        return JsonResponse(public_methods.response_message(result, response, result_code))
