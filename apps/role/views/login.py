# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from apps.role import models as mysql_db
from apps.role.views import public_methods
from django.http import JsonResponse


@csrf_exempt
def user_login(request):

    if request.method == 'POST':

        post = request.POST
        user_name = post["userName"]
        password = post["password"]

        check_validity = mysql_db.Person.objects.get(user_name=user_name)
        # check_validity = mysql_db.Person.objects.filter(user_name=user_name).values('user_id', 'user_type')

        if check_validity.password == password:

            user_id = check_validity.user_id
            user_type = check_validity.user_type

            response_message = {"message": "登陆成功", "userId": user_id, "userType": user_type}

            response = public_methods.response_message("success", response_message, "100001")

            return JsonResponse(response)
