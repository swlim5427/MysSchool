# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from apps.class_manager import models as mysql_db
from public import public_methods
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import time


@csrf_exempt
def class_list(request):

    # curriculum_list_j = ""

    if request.method == 'POST':
        post = request.POST

        week = post["week"]
        assortment_type = post["assortmentType"]
        class_id = []

        time.sleep(0.01)

        get_class_list = mysql_db.ClassInfo.objects.filter(status="1", class_week=week, assortment_type=assortment_type)

        print get_class_list.values("class_student")

        try:
            check_class_list = get_class_list.values()[0]

            class_list_j = serializers.serialize('json', get_class_list)

        except:

            response = public_methods.response_message("success", "", "100001")

            return JsonResponse(response)

        for i in range(len(get_class_list.values())):

            class_id.append(get_class_list.values()[i]["class_id"])

        response = class_list_j.encode('utf-8')
        return HttpResponse(response)