from __future__ import unicode_literals
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from apps.role import models as mysql_db
from django.db.models import Q
import json
import time


@csrf_exempt
def teacher_list(request):

    if request.method == 'POST':

        post = request.POST

        get_teacher_list = mysql_db.Teacher.objects.filter(status=1).filter(teach_type=1).values('name', 'user_id')

        teacher_list_r = json.dumps(list(get_teacher_list))
        return HttpResponse(teacher_list_r)