# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from C1.models import *

def dbview(reqeust):
    flist = Category.objects.filter(c_father = 0)
    clist = []
    for f in flist:
        clist.append(Category.objects.filter(c_father = f.id))
    
     
    return render_to_response('dbview.html',locals())

def category_list(request):
    if request.GET.has_key('sid'):
        s_id = request.GET['sid']
        father_category = get_object_or_404(Category,pk=s_id)
        c_list = Category.objects.filter(c_father=s_id)
    return render_to_response('category_list.html',locals())