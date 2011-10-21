# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template import context
from django.http import Http404,HttpResponse
import datetime


def helloworld(request):
    return HttpResponse("Hello World! ")

def current_datetime(reqeust,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours = offset)
    #html = "<html><title>Current Time</title><body>The local time is now <h2>%s</h2>. And the time you want is <h2>%s</h2></body></html>" %(now,dt)
    #return HttpResponse(html)
    return render_to_response('t1.html',locals())