# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.role import models as mysql_db
from public import public_methods


@csrf_exempt
class UserRegist:

    def __init__(self, request):

        if request.method == 'POST':

            post = request.POST
            self.user_check = public_methods.user_check(post)
            self.user_id = ""
            self.user_type = ""
            self.user_regist()

    def user_regist(self):

        if self.user_check == 1:

            if self.user_type == 1:
                try:
                    self.user_id = mysql_db.Person.objects.order_by('-user_id')[0].user_id
                except:
                    self.user_id = "10000001"
            elif self.user_type == 2:
                try:
                    self.user_id = mysql_db.Person.objects.order_by('-user_id')[0].user_id
                except:
                    self.user_id = "20000001"

            user_name = self.post['userName']
            password = self.post['password']
            self.user_type = self.param['userType']

            regist_persion = mysql_db.Person(
                user_id=self.user_id,
                user_name=user_name,
                password=password,
                user_type=self.user_type,
                create_time=public_methods.get_date_time(1, 1),
                update_time=public_methods.get_date_time(1, 1),
                status=0,

            )

            regist_persion.save()
            response = {"message": "注册成功", "userId": self.user_id, "userType": self.user_type}

            if self.user_type == "1":

                return HttpResponse(public_methods.response_message("success", response, "100001"))

            elif self.user_type == "2":

                return HttpResponse(public_methods.response_message("success", response, "100002"))

        elif self.user_check == 0:

            response = "注册失败,用户已存在"

            if self.user_type == "1":

                return HttpResponse(public_methods.response_message("fault", response, "100003"))

            elif self.user_type == "2":

                return HttpResponse(public_methods.response_message("fault", response, "100004"))
