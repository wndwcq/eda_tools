#-*- coding: UTF-8 -*-
"""

"""
from django.shortcuts import render
#---  my code --------------------------
from django.template import Template,Context
from django.template.loader import get_template
from django.http import HttpResponse
from kb.models import Record
from kb.forms import RecordForm
from django.shortcuts import  render_to_response,render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import datetime
import logging

# Create your views here.
logger = logging.getLogger('my_log')
use_logger = logging.getLogger('use_log')
search_logger = logging.getLogger('search_log')

def kb_home(request):
    # 记录使用日志
    use_logger.debug("KB" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
    
    if not request.user.is_authenticated():       #非授权用户不得访问该模块        
        # 记录使用日志
        use_logger.debug("KB:AccessDenied:NoAuth" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])        
        return HttpResponseRedirect("/index/")
        
    # --------对查询条件进行查询------------
    if request.GET.get('what'):
        #有查询条件进行填写的情况下，按照查询条件进行查询
        #     记录搜索日志
        search_logger.debug(request.GET.get('what') + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
        # 将搜索字符串按照空格进行分离
        search_list = request.GET.get('what').split(' ')
        
        is_first = 1     
        for aSearch in search_list:
            if is_first == 1:
                allrows=Record.objects.all().order_by("-update_time").filter(status=1).filter(summary__contains=aSearch)
                is_first +=1
            else:
                allrows = allrows.filter(summary__contains=aSearch)            
    #    allrows = allrows.filter(summary__contains=request.GET.get('what'))
    else:
        # 无查询条件时，给出所有的结果
        allrows=Record.objects.all().order_by("-update_time").filter(status=1)
    #--------------------------------------------
    
    #--------分页操作--------------------------
    paginator = Paginator(allrows,4)
    page = request.GET.get('page')
    try:
        record = paginator.page(page)
    except PageNotAnInteger:
        record = paginator.page(1)
    except EmptyPage:
        record = paginator.page(paginator.num_pages)
    #--------------------------------------------
    
    # 对查询条件框的值进行初始化
    if request.GET.get('what') == None:
        search = ""
    else:
        search = request.GET.get('what')
                
    return render_to_response('temp_kb_main.html',{'allRow':record,'search':search,\
                                                   'request':request,'is_login':request.user.is_authenticated()})


def add_a_kb_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if not form.is_bound :
            return HttpResponse('<html><body><a href = "/kb/">ERROR:数据绑定异常</a></body></html>')
        
        if form.is_valid():
            cd = form.cleaned_data
            logger.debug(cd['detail'])
            p = Record(title = cd['title'],detail = cd['detail'],summary = cd['summary'],creat_time =datetime.datetime.now(),\
					update_time = datetime.datetime.now(),contrib_id = 1,contrib = request.user,status = 1,addi_file = cd['addi_file'],\
                    evaluation_time = 0,good_time = 0)
            p.save()            
            # 记录使用日志
            use_logger.debug("KB:AddRec:OK:ID=" + str(p.id) + "-" + request.user.username + "-" + request.META['REMOTE_ADDR']) 
            html = '<html><body><a href = "/kb/">操作成功</a></body></html>'
            return HttpResponse(html)
        else:
            # 记录使用日志
            use_logger.debug("KB:AddRec:Fail:NoMessage" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR']) 
            return HttpResponse('<html><body><a href = "/kb/">ERROR:数据填写不全，请检查后提交</a></body></html>')
    else:
        form = RecordForm()
        return render_to_response('temp_form.html',{'form':form,'acction_page':'/add_a_kb_record/','button_value':'提交记录'})


# -----修改记录------------------
def update_a_kb_record(request): 
    if request.method == 'GET':               
        row_no = request.GET.get('Row')
        p = Record.objects.get(id = row_no)
        
        if  p.contrib != request.user.username :        #限制用户只能修改自己的记录
            return HttpResponse('<html><body><a href = "/kb/">ERROR:您无权修改这条记录</a></body></html>')
        
        form = RecordForm(initial={'id':row_no,'title':p.title,'detail':p.detail,'summary':p.summary,'addi_file':p.addi_file})     
        return render_to_response('temp_form.html',{'form':form,'acction_page':'/add_a_kb_record/','button_value':'提交修改'})
    
    #----- --------------
    elif request.method == 'POST':           
        form = RecordForm(request.POST,request.FILES)
        
        if not form.is_bound:
            return HttpResponse('<html><body><a href = "/kb/">ERROR:数据绑定异常</a></body></html>')
        
        if form.is_valid():
            cd = form.cleaned_data
            logger.debug(cd['detail'])
            p = Record.objects.get(id = cd['id'])
            #-------------
            p.title = cd['title']
            p.summary = cd['summary'] 
            p.detail = cd['detail'] 
            p.addi_file = cd['addi_file'] 
            p.update_time = datetime.datetime.now()              
            
            p.save()            
            #-----------------------------
            # 记录使用日志
            use_logger.debug("KB:UpdateRec:OK:ID=" + str(p.id) + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
            return HttpResponse('<html><body><a href = "/kb/">操作成功</a></body></html>')
        else:
            # 记录使用日志
            use_logger.debug("KB:UpdateRec:Fail:NoMessage" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
            return HttpResponse('<html><body><a href = "/kb/">ERROR:数据填写不全，请检查后提交</a></body></html>')
        
    return HttpResponseRedirect('/kb/')

def delete_a_kb_record(request):   
    if request.method == 'GET':
        row_no = request.GET.get('Row')
        p = Record.objects.get(id = row_no)
        p.status = 0
        p.save()
        return HttpResponse('<html><body><a href = "/kb/">删除成功</a></body></html>')
    return HttpResponse('<html><body><a href = "/kb/">ERROR:调用异常</a></body></html>')     

#   知识库的记录进行点赞数量的累加    
def kb_make_a_thumb(request):
    if request.is_ajax():
        row_no = request.GET.get('kbid')
        p = Record.objects.get(id = row_no)
        p.good_time += 1
        p.save()
        # 记录使用日志
        use_logger.debug("KB:MakeThumb:OK" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'] + "thumb record_id = " + str(p.id))
    return