# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from apps.role import models as mysql_db
from apps.role.views import public_methods
from django.http import JsonResponse


@csrf_exempt
def user_info(request):

    if request.method == 'POST':

        post = request.POST
        user_id = post["userId"]

        get_user_info = mysql_db.Person.objects.get(user_id=user_id)

        user_id = get_user_info.user_id
        user_type = get_user_info.user_type

        if get_user_info.user_type == "0":

            user_id = get_user_info.user_id
            user_type = get_user_info.user_type

            response_message = {"message": "登陆成功", "userId": user_id, "userType": user_type}

            response = public_methods.response_message("success", response_message, "100001")

            return JsonResponse(response)
