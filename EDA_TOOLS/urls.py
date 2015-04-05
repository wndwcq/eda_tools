#-*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url

from django.conf import settings
#------------------------------------------------
from django.contrib import admin
admin.autodiscover()

#----------- and by weining for this app ------------
from kb.views import add_a_kb_record,kb_home,update_a_kb_record,kb_make_a_thumb
from sys_views import home,logout_view,user_regist_view,change_pwd_view
#----------------------------------------------------



urlpatterns = patterns('',
                       (r'^site_static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),             
                       (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),                           
    # Examples:
    # url(r'^$', 'EDA_TOOLS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #----------- add by this app -----------------
    url(r'^index/$',home), 
    url(r'^kb/$',kb_home),  
    url(r'^add_a_kb_record/$',add_a_kb_record),     #-- 添加一条知识库记录---
    url(r'^update_a_kb_record/$',update_a_kb_record),
    url(r'^logout/$',logout_view),
    url(r'^regist/$',user_regist_view),
    url(r'^change_pwd',change_pwd_view),
    url(r'^kb_make_thumb',kb_make_a_thumb),
)
