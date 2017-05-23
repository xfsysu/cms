from django.conf.urls import url,include
from . import views

app_name = 'union'

urlpatterns = [
	#/union/
    url(r'^$', views.index, name='index'),

    #/union/<union_id>/detail
    url(r'^(?P<union_id>[0-9]+)/detail/$', views.detail, name='detail'),

    #/union/union_add/
    url(r'^union_add/$', views.union_add, name='union_add'),

    #/union/view_all
    url(r'^view_all/$', views.view_all, name='view_all'),

    #/union/login_user
    url(r'^login_user/$', views.login_user, name='login_user'),
    
    #/union/register
    url(r'^register/$', views.register, name='register'),

    #/union/logout_user
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    #/union/<union_id>/union_delete
    url(r'^(?P<union_id>[0-9]+)/union_delete/$', views.union_delete, name='union_delete'),

    #/union/<union_id>/member_add
    url(r'^(?P<union_id>[0-9]+)/member_add/$', views.member_add, name='member_add'),

    #/union/<member_id>/member_delete
    url(r'^(?P<member_id>[0-9]+)/member_delete/$', views.member_delete, name='member_delete'),

    #/union/<member_id>/member_edit
    url(r'^(?P<member_id>[0-9]+)/member_edit/$', views.member_edit, name='member_edit'),
]
