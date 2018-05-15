# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.curriculum import models as mysql_db
from pubulic import public_methods
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import time


@csrf_exempt
def curriculum_list(request):

    curriculum_list_j = ""

    if request.method == 'POST':
        post = request.POST

        # curriculum_id = post["curriculum_id"]

        time.sleep(0.01)

        get_curriculum_list = mysql_db.Curriculum.objects.filter(status="1")

        try:
            curriculum = get_curriculum_list.values()[0]

            curriculum_list_j = serializers.serialize('json', get_curriculum_list)

            response = curriculum_list_j
            return HttpResponse(response)

        except:

            response = public_methods.response_message("success", "", "100001")

            return JsonResponse(response)


@csrf_exempt
def assortment_list(request):

    if request.method == 'POST':
        post = request.POST

        try:
            assortment_id = post["assortmentId"]
            get_assortment_name = mysql_db.Assortment.objects.get(assortment_id=assortment_id)
            assortment_name = get_assortment_name.assortment_name
            response = assortment_name

        except:

            get_assortment_list = mysql_db.Assortment.objects.all()

            assortment_list_j = serializers.serialize('json', get_assortment_list)

            response = assortment_list_j

        return HttpResponse(response)
