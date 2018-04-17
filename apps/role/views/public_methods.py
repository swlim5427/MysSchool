# -*- coding: utf-8 -*-

from apps.role import models as mysql_db
import datetime
import time


def user_check(param):

    user_name = param["userName"]
    user_check = mysql_db.Person.objects.filter(user_type=user_name)
    if user_check == "":
        return 1
    else:
        return 0


def get_date_time(file_name, now_time):

    date_time = datetime.datetime.now()

    if file_name == 1 and now_time == 0:

        input_year = date_time.year
        input_month = date_time.month
        input_day = date_time.day
        input_hour = date_time.hour
        input_minute = date_time.minute
        input_second = date_time.second
        microsecond_time = date_time.microsecond

        imput_datetime = datetime.datetime(
                year=int(input_year),
                month=int(input_month),
                day=int(input_day),
                hour=int(input_hour),
                minute=int(input_minute),
                second=int(input_second)
        )
        format_time = long(round(time.mktime(imput_datetime.timetuple())))

        now_time = long(str(format_time) + str(microsecond_time/1000))

        return now_time

    else:
        return date_time


def response_message(result, message, code):

    http_response ={"result": result, "responseMessage": message, "code": code}

    return http_response
