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
from apps.role.views import regist
from apps.role.views import login
from apps.role.views import update_user_info
from apps.role.views import get_user_info
from apps.role.views import user_info


urlpatterns = [

    url(r'^user_regist/$', regist.UserRegist),
    url(r'^user_login/$', login.user_login),
    url(r'^update_user_info/$', update_user_info.UserInfo),
    url(r'^user_info/$', user_info.user_info),
    url(r'^get_user_info/$', get_user_info.get_user_info),

    url(r'^admin/', admin.site.urls),
]
