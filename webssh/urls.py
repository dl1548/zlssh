#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
'''

from . import views
from django.urls import path,include

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('login',views.SSHLogin,base_name='webssh_login')
router.register('history',views.TerminalHistory,base_name='webssh_history')

urlpatterns = [
    path('', include(router.urls)),
]