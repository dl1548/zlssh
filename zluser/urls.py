#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
'''


from django.urls import path,include
from . import views
from .views import UserLogin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('list', views.UserList,base_name='user_list')
router.register('info', views.UserInfo,base_name='user_info')
router.register('logout', views.UserLogout,base_name='user_logout')

urlpatterns = [
    path('login/', UserLogin.as_view(), name='user_login'), # 方法重写, 刷新可借鉴  
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]
