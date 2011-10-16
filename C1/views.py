# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from C1.models import *

def dbview(reqeust):
    Man_list = Man.objects.all()
    return render_to_response('dbview.html',locals())