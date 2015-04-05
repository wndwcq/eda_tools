#-*- coding: UTF-8 -*-

from django.shortcuts import render,render_to_response
#---  my code --------------------------
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from forms import RegistForm,ChangePwdForm

#---  add by weining --- my view -----------------------
import logging

use_logger = logging.getLogger('use_log')

def home(request):    
    message = ""
    # 记录使用日志
    use_logger.debug("Home" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
    
    if request.method == 'POST':
        # 记录使用日志
        use_logger.debug("Login" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
        
        # 用户登录验证
        user_name = request.POST['uname']
        user_pwd = request.POST['upwd']
        user = authenticate(username=user_name,password=user_pwd)            

        if user is not None:
            if user.is_active:
                login(request,user)
                message ="user:"+ user_name
                
                # 记录使用日志
                use_logger.debug("Login:OK" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
                
            else:
                message = "该用户暂未激活，请联系系统管理员"
                # 记录使用日志
                use_logger.debug("Login:Fail:ActiveFalse" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
        else:
            message = "用户名及密码不正确，请确认后输入"
            # 记录使用日志
            use_logger.debug("Login:Fail:UnameOrPwdError" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
        
    return render_to_response('temp_index.html',{'request':request,'is_login':request.user.is_authenticated(),'message':message})

def logout_view(request):
     # 记录使用日志
    use_logger.debug("Logout" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
    
    logout(request)   
    return HttpResponseRedirect("/index/")


#----- 用户注册 view ------------------------
def user_regist_view(request):
    form = RegistForm()
    return render_to_response('temp_form.html',{'form':form})
#-----------------------------------------

#----修改密码 view------------------------
def change_pwd_view(request):
    if request.method == 'POST':
        # 记录使用日志
        use_logger.debug("ChangePwd" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
            
        form = ChangePwdForm(request.POST)
        if not form.is_bound :
            return HttpResponse('<html><body><a href = "/index/">ERROR:数据绑定异常</a></body></html>')
        
        if form.is_valid():
            cd = form.cleaned_data
            now_pwd = cd['old_pwd']
            if request.user.check_password(now_pwd) and (cd['new_pwd']==cd ['con_pwd']):
                request.user.set_password(cd['new_pwd'])
                request.user.save()
                
                # 记录使用日志
                use_logger.debug("ChangePwd:OK" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])
                
                return HttpResponse('<html><body><a href = "/index/">密码修改成功</a></body></html>')
        
        # 记录使用日志
        use_logger.debug("ChangePwd:Fail:noMessage" + "-" + request.user.username + "-" + request.META['REMOTE_ADDR'])                            
        return HttpResponse('<html><body><a href = "/index/">ERROR:信息填写不完整或信息不正确</a></body></html>')
    else:
        form = ChangePwdForm()
        return render_to_response('temp_form.html',{'form':form,'button_value':'保存修改','action_page':''})