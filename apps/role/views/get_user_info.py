from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def get_user_info(request):

    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)