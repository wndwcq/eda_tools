#-*- coding: UTF-8 -*-

from django import forms

class RecordForm(forms.Form):
    id = forms.IntegerField(widget = forms.HiddenInput,required = False )
    status = forms.IntegerField(widget = forms.HiddenInput,required = False)
    title   = forms.CharField(max_length = 24,label="主题",widget=forms.Textarea(attrs={'cols':'100','rows':'1'}))
    summary = forms.CharField(max_length = 512,label = "摘要",widget=forms.Textarea(attrs={'cols':'100','rows':'2'}))
    detail  = forms.CharField(max_length = 4096,label="内容",widget=forms.Textarea(attrs={'cols':'100','rows':'15'}))
    addi_file = forms.FileField(max_length = 200,label = "附件",required = False,)

