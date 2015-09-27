# -*-coding:utf-8-*-
from django.db import models

# Create your models here.
class answers(models.Model):
    SN = models.CharField(max_length=18,primary_key=True) #编号，主键
    m_name = models.TextField(null=True) #商户名称
    m_address = models.TextField(null=True) #商户地址
    m_phone = models.IntegerField(null=True) #商户联系电话
    isoverbank = models.NullBooleanField(null=True) #是否开通跨行
    iscredit = models.NullBooleanField(null=True) #是否开通贷记卡
    isbaobei = models.NullBooleanField(null=True) #是否报备
    islow = models.NullBooleanField(null=True) #是否无效户
    #开始问卷答案部分
    Q_version = models.TextField(null=True)
    Q_overbank = models.TextField(null=True)
    Q_iscredit = models.TextField(null=True)
    Q_baobei = models.TextField(null=True)
    Q1_most = models.CharField(max_length=20,null=True) #最常用机具
    Q2_choice = models.CharField(max_length=1,null=True) #问题 不使用农行机具原因
    Q2_text = models.TextField(null=True) #其他内容：
    Q3_choice = models.CharField(max_length=1,null=True)  # 问题 不使用农行机具原因
    Q3_text = models.TextField(null=True)
    hly = models.CharField(max_length=19,null=True)
    name = models.TextField(null=True)
    sex = models.CharField(max_length=1,null=True)
    phone= models.IntegerField(null=True)
    isdone = models.NullBooleanField(null=True)  # 是否已完成
    def __str__(self):
        return self.SN
