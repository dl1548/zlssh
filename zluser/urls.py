#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
'''


from django.urls import path,include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('list', views.UserList,base_name='user_list')

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]
