#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
'''




from django.urls import path,include
from . import views


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('list', views.HostList,base_name='host_list')

urlpatterns = [
    path('', include(router.urls)),
]
