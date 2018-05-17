# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.curriculum import models as mysql_db
from pubulic import public_methods
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def class_edit(request):

    if request.method == 'POST':
        post = request.POST

        curriculum_name = post["curriculumName"]
        assortment_id = post["assortmentId"]
        curriculum_id = post["curriculumId"]
        status = post["status"]

        update_curriculum = mysql_db.Curriculum.objects.get(curriculum_id=curriculum_id)

        update_curriculum.status = status
        update_curriculum.curriculum_name = curriculum_name
        update_curriculum.assortment_id = assortment_id

        try:

            update_curriculum.save()

            if status == "0":
                r_text = "删除成功"
            else:
                r_text = "修改成功"
            response = {"message": r_text, "curriculumId": curriculum_id}
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

        return JsonResponse(public_methods.response_message(result, response, result_code))
