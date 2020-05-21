from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from TestWeb import activity


def requestget(request):
    # if request.POST.get('button')=='配点json':
    #     return render(request, "json_form.html", {'aa':'aaa'})
    return render(request, "main.html", {'aa':'aaa'})
