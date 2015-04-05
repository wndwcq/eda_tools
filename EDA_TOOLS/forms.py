#-*- coding: UTF-8 -*-
"""
"""
from django import forms

#----------注册 form------
class RegistForm(forms.Form):
    acc = forms.CharField(max_length = 30,label="昵称")
    name = forms.CharField(max_length = 30,label="姓名")
    depart = forms.CharField(max_length = 64,label="部门")
    mobil = forms.CharField(max_length = 13,widget = forms.NumberInput,label="手机")
    mail = forms.EmailField(max_length = 30,min_length = 10,label="邮箱")
    password1 = forms.CharField(max_length = 8,widget = forms.PasswordInput,label="密码")
    password2 = forms.CharField(max_length = 8,widget = forms.PasswordInput,label="确认")  
  
#----------------------------

#---------修改密码 forms--------
class ChangePwdForm(forms.Form):
    old_pwd = forms.CharField(max_length = 8,widget = forms.PasswordInput,label = "现密码")
    new_pwd = forms.CharField(max_length = 8,widget = forms.PasswordInput,label = "新密码")
    con_pwd = forms.CharField(max_length = 8,widget = forms.PasswordInput,label = "密码确认")
#-----------------------------