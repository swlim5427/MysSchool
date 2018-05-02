# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.curriculum import models as mysql_db
from pubulic import public_methods
from django.http import HttpResponse


def curriculum_add(request):

    if request.method == 'POST':
        post = request.POST

        curriculum_name = post["userName"]
        assortment_id = post["assortmentId"]

        try:
            curriculum_id = mysql_db.Curriculum.objects.order_by('-curriculum_id')[0].user_id
        except:
            curriculum_id = "c0000001"

        add_curriculum = mysql_db.Curriculum(
            curriculum_name=curriculum_name,
            assortment_id=assortment_id,
            curriculum_id=curriculum_id

        )

        add_curriculum.save()

        response = {"message": "课程创建成功", "curriculumId": curriculum_id}

        return HttpResponse(public_methods.response_message("success", response, "100001"))
