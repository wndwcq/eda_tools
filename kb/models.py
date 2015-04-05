#-*- coding: UTF-8 -*-

from django.db import models

# Create your models here.

class Record (models.Model):    # 知识库记录
    title   = models.CharField(max_length = 256)  #标题
    summary = models.CharField(max_length = 512) #摘要
    detail  = models.TextField()                 #内容详情
    creat_time = models.DateTimeField()          #创建时间
    update_time = models.DateTimeField()         #修改时间
    contrib_id = models.IntegerField(null = True)#贡献人ID
    contrib = models.CharField(max_length = 30)   #贡献人    
    status = models.IntegerField()                #记录状态 0 无效  1 有效
    evaluation_time = models.IntegerField(null = True) #对该记录的评价的次数 
    good_time = models.IntegerField(null = True)   #点赞的次数    
    addi_file = models.FileField(max_length = 200,null = True)   #附件
    
    def __unicode__(self):
        return self.title
    
class Tag(models.Model):        # tag   
    tag_name = models.CharField(max_length = 32)
    tag_desc = models.CharField(max_length = 256,null = True)
    
class Tag_Rec(models.Model):    #记录知识库记录和tag的关系
    tag = models.IntegerField()
    rec = models.IntegerField()
