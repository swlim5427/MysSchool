# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.role import models as mysql_db
from public import public_methods


@csrf_exempt
def user_login(request):

    if request.method == 'POST':

        post = request.POST
        user_name = post["userName"]
        password = post["password"]

        try:

            check_validity = mysql_db.Person.objects.get(user_name=user_name)
            # check_validity = mysql_db.Person.objects.filter(user_name=user_name).values('user_id', 'user_type')

            if check_validity.password == password:

                user_id = check_validity.user_id
                user_type = check_validity.user_type

                response_message = {"message": "登陆成功", "userId": user_id, "userType": user_type}

                response = public_methods.response_message("success", response_message, "100001")

                # user_info.get_user_info((user_id, user_type))

                return JsonResponse(response)

            else:
                response = {"message": "用户名或密码错误"}
                return JsonResponse(public_methods.response_message("fault", response, "100005")).set_cookie("abc", "1")

        except:

            response = {"message": "用户名或密码错误"}
            return JsonResponse(public_methods.response_message("fault", response, "100005")).set_cookie("sessionid", "1111")
