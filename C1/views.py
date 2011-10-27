# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404,HttpResponseRedirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import simplejson
from C1.models import *
from C1.cform import *


def dbview(reqeust):
    flist = Category.objects.filter(c_father = 0)
    clist = []
    for f in flist:
        clist.append(Category.objects.filter(c_father = f.id))
    tlist = zip(flist,clist) #将原有分散的2个列表ZIP到1个总列表,在表现层就不用到for循环中去验证与父循环ID的匹配,节省开销
    return render_to_response('dbview.html', {'tlist':tlist} )

def category_list(request):
    if request.GET.has_key('sid'):
        s_id = request.GET['sid']
        father_category = get_object_or_404(Category,pk=s_id)
        c_list = Category.objects.filter(c_father=s_id)
    return render_to_response('category_list.html',locals())

def form_test(request):
    if request.method == 'POST':
        form = Staffe_info(request.POST,request.FILES)
        if form.is_valid():
            #print request.FILES
            #SimpleUploadedFile(request.FILES['up'])
            return HttpResponseRedirect('/hello')
    else:
        form = Staffe_info()
    return  render_to_response('form.html',locals())

def city_list(request):
    city_list = []
    province = request.GET['provinceID']
    citys = City.objects.filter(provinceID = province)
    for city in citys:
        c = {}
        c['label'] = city.cityName
        c['text'] = city.id
        city_list.append(c)
    return HttpResponse(simplejson.dumps(city_list), mimetype='application/json')

def category_jlist(request):
    jsonclist = []
    cjlist = Category.objects.filter(c_hidden=0)
    for cj in cjlist:
        c = {}
        c['id'] = cj.id
        c['pId'] = cj.c_father
        c['name'] = cj.c_name
        if (cj.c_father==0):
            c['open'] = True
        jsonclist.append(c)
    return HttpResponse(simplejson.dumps(jsonclist), mimetype='application/json')

import codecs
def category_manage(request):
    if request.GET.has_key('mode'):
        mode = request.GET['mode']
        if mode == 'reset':
            jfile = codecs.open('static/js/category_data.js','w','utf-8')#Python3.0以上版本可以直接使用f.open(...,'encoding':'utf-8')
            jfile.write("var array=new Array();\n")
            clist = Category.objects.all()
            for c in clist:
                jfile.write ("array[%d]=new Array('%d','%d','%s')\n"%(c.id-1,c.id,c.c_father,c.c_name))
            jfile.close()
    return render_to_response('category.html',locals())


def category_reconstruct(request):
    if request.method == 'POST':
        clist = eval(request.raw_post_data);

        cid_list = [];
        cid_old_list=[]
        for c in clist:
             cid_list.append(c['id'])

        c_old = Category.objects.all()
        for cd in c_old:
            cid_old_list.append(cd.id)

        cid_old_list.sort()
        cid_list.sort()

        cid_old_list_set = set(cid_old_list)
        cid_list_set = set(cid_list)

        #更新分类数据
        cid_list_x = cid_old_list_set & cid_list_set #提取更新部分ID
        c1 = Category.objects.filter(id__in=cid_list_x)#初步筛选
        for c in clist:
            try:
                c1c = c1.get(id=c['id'])
                if (c1c.c_name != unicode(c['name'],'UTF-8') or c1c.c_father!=c['pId']):#加入判断，减少数据库写操作
                    c1c.c_name=unicode(c['name'],'UTF-8')
                    c1c.c_father=c['pId']
                    c1c.save()
            except Exception as error:#因新分类库可能大于原有分类库，故会出现"not exist"错误，在此抛出
                #print error
                continue

        #删除分类
        cid_list_x = cid_old_list_set - cid_list_set #提取被删除部分ID
        Category.objects.filter(id__in=cid_list_x).update(c_hidden=True)


        #新增分类
        cid_list_x = cid_list_set - cid_old_list_set #提取新增部分ID
        for c in clist:
            try:
                cid_list_x.remove(c['id'])#set无直接索引办法，故使用删除，然后异常抛出处理
                c_add = Category(c_name=unicode(c['name'],'UTF-8'),c_father=c['pId'])
                c_add.save()
                for i in range(len(clist)):#更新原始数据中的pId值，避免数据库开销
                    if clist[i]['pId'] == c['id']:
                        clist[i]['pId'] = c_add.id
            except Exception as error:
                #print error
                continue
    return render_to_response('t1.html',locals())
        