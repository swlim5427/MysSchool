"""MysSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apps.role.views import regist, login, update_user_info, get_user_info, user_info, user_list, student_add
from apps.curriculum.views import curriculum_add, curriculum_list, curriculum_edit
from apps.class_manager.views import class_add, class_list, class_edit, class_eliminate, period_statistics


urlpatterns = [

    url(r'^user_regist/$', regist.UserRegist),
    url(r'^user_login/$', login.user_login),
    url(r'^update_user_info/$', update_user_info.UserInfo),
    url(r'^user_info/$', user_info.user_info),
    url(r'^g/$', get_user_info.get_user_info),
    url(r'^curriculum_add/$', curriculum_add.curriculum_add),
    url(r'^curriculum_list/$', curriculum_list.curriculum_list),
    url(r'^assortment_list/$', curriculum_list.assortment_list),
    url(r'^curriculum_edit/$', curriculum_edit.curriculum_edit),
    url(r'^class_list/$', class_list.class_list),
    url(r'^class_add/$', class_add.class_add),
    url(r'^class_edit/$', class_edit.class_edit),
    url(r'^class_eliminate/$', class_eliminate.class_eliminate),
    url(r'^period_statistics/$', period_statistics.period_statistics),
    url(r'^user_list/$', user_list.user_list),
    url(r'^student_add/$', student_add.student_add),

    url(r'^admin/', admin.site.urls),
]
