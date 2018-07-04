# -*- coding: utf-8 -*-
#
# from __future__ import unicode_literals
#
# # from django.http import JsonResponse
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# # from django.forms.models import model_to_dict
# from django.core import serializers
# from django.shortcuts import render_to_response
# from apps.role import models as mysql_db
# # from public import public_methods
#
#
# @csrf_exempt
# def get_user_info(request):
#
#     # if request.method == 'GET':
#
#     get_user_info = mysql_db.Teacher.objects.all()
#
#     a = get_user_info.values()
#     b = serializers.serialize('json', get_user_info)
#     #
#     # for item in a:
#     #    item
#     # a = {"key":get_user_info.values()}
#     return HttpResponse(b)
#     # return JsonResponse(a)
#
import os
from django.shortcuts import render
from django.http.response import JsonResponse


# global inventory_path
# inventory_path = "../playbooks/IDC-group/EagleFinancial"


def get_user_info(request):

    context = {'a': "123", "b": "456", "c": "789", "d": "4321"}
    # context['a'] = '1'

    # return render(request, 'main.html', context)

    return render(request, 'index.html', context)
# def getNode(request):
#
#     res = []
#
#     for dir_name in os.listdir(inventory_path):
#         res.append(dir_name)
#
#     return JsonResponse(res)
