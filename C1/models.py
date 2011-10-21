# -*- coding: UTF-8 -*-
from django.db import models

class Man(models.Model):
    sid = models.CharField(max_length=18,help_text="身份证号")
    name = models.CharField(max_length=10)
    tname = models.CharField(max_length=10)
    category = models.CharField(max_length=2,choices=(
        ('1', '贩毒人员'),
        ('2', '贩毒嫌疑人员'),
        ('3','吸毒人员'),
        ('4','吸毒嫌疑人员'),
        ('5','其他涉毒人员'),
        ('6','一般人员'),
        ('7','无法确定'))
    )

class CellDB(models.Model):
    number = models.CharField(max_length=11)
    owner= models.ForeignKey(Man)

class Category(models.Model):
    c_name = models.CharField(max_length=20,help_text="类别名称")
    c_father = models.IntegerField(max_length=4,default=0,help_text="父级类别ID，目前系统容量为10000个类别")

    def __unicode__(self):
        return (u'%d,%s') % (self.c_father,self.c_name)
