# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.curriculum import models as mysql_db
from pubulic import public_methods
from django.http import HttpResponse
from django.http import JsonResponse


def curriculum_add(request):

    if request.method == 'POST':
        post = request.POST

        curriculum_id = post["curriculum_id"]

        get_curriculum_list = mysql_db.Curriculum.objects.all()

        return HttpResponse(public_methods.response_message("success", get_curriculum_list.values(), "100001"))
