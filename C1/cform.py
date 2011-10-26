# -*- coding: UTF-8 -*-
from django import forms
from C1.models import Province,Category

class Staffe_info(forms.Form):
    name = forms.CharField(max_length=10,min_length=2,label='姓名',error_messages={'required': '缺至时自定义错误','min_length':'最小长度自定义错误'})
    pwd = forms.CharField(max_length=10,widget=forms.PasswordInput)
    shop = forms.ChoiceField(
         choices = ([('1','aaaaaaa'), ('2','bbbbbbbb'),('3','ccccccccc') ]), initial='2', required = True,)
    shop2 = forms.ModelChoiceField(queryset=Category.objects.filter(c_father=0),empty_label="请选择分类",label='',required=False)
    tp = forms.TypedChoiceField(coerce=bool,choices=((False, 'False'), (True, 'True')),widget=forms.RadioSelect,required=False) #coerce指定数据类型，比如也可以定义为int
    mchoice = forms.MultipleChoiceField(choices=(("a", "1"), ("b", "2"), ("c", "3")),widget=forms.CheckboxSelectMultiple(),initial=('a','b'),required=False) #表现和定义的不同
    up = forms.FileField()

provinces = Province.objects.all()
PROVINCE_CHOICES = []
for province in provinces:
    PROVINCE_CHOICES.append([province.id, province.provinceName])
class myForm(forms.Form):
    province = forms.ChoiceField(widget = forms.Select(attrs={'class':'select', 'onChange':'getCityOptions(this.value)'}), choices = PROVINCE_CHOICES, label= u'选择省')
    city = forms.ChoiceField(widget = forms.Select(attrs={'class':'select', 'onChange':'getDistrictOptions(this.value)','style':'display:none'}), label = u'选择市')