# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from public import public_methods
from django.db.models import Count
from apps.class_manager import models as mysql_db
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def commit_period(request):

    if request.method == 'POST':

        post = request.POST

        print post
