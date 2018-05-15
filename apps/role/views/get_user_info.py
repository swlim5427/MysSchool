# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers

from apps.role import models as mysql_db
from pubulic import public_methods


@csrf_exempt
def get_user_info(request):

    # if request.method == 'GET':

    get_user_info = mysql_db.Teacher.objects.all()

    a = get_user_info.values()
    b = serializers.serialize('json', get_user_info)
    #
    # for item in a:
    #    item
    # a = {"key":get_user_info.values()}
    return HttpResponse(b)
    # return JsonResponse(a)

