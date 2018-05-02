# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.role import models as mysql_db
from pubulic import public_methods


@csrf_exempt
def get_user_info(request):

    if request.method == 'GET':

        get_user_info = mysql_db.Person.objects.all()

        return HttpResponse(get_user_info.values())

