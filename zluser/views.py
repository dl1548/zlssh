#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
'''


from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from django.contrib.auth.models import User
from utils.return_code import zlreturn

from rest_framework.permissions import IsAuthenticated #, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins

from . import serializers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        
        return zlreturn(1000,data)

class UserLogin(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserLogout(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.NullARGSSerializer
    # permission_classes = (IsAuthenticated,)

    def create(self, request):
        get_serializer = self.get_serializer(data=request.data)
        get_serializer.is_valid(raise_exception=True)
        post_data = get_serializer.validated_data

        print('user  logout------------')

        return JsonResponse(zlreturn(1000,{'aaa':'logout'}) ,safe=False)  

class UserInfo(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.UserListAPISerializer
    # permission_classes = (IsAuthenticated,)


    def list(self, request):
        # get_serializer = self.get_serializer(data=request.data)
        # get_serializer.is_valid(raise_exception=True)
        # post_data = get_serializer.validated_data
        # print('userinfo------------')

        # get_serializer = serializers.UserListSerializer(queryset, many=True)
        
        test_data = {
            'name' : 'admin',
            'avatar' : 'admin'
        }
        return JsonResponse(zlreturn(1000,test_data) ,safe=False)

    def create(self, request):
        get_serializer = self.get_serializer(data=request.data)
        get_serializer.is_valid(raise_exception=True)
        post_data = get_serializer.validated_data

        if post_data:
            try:
                # queryset = User.objects.filter(username=post_data["username"])
                queryset = User.objects.filter(username='admin')
                get_serializer = serializers.UserListSerializer(queryset, many=True)
            except Exception as e:
                return JsonResponse(e)
        else:
            try:
                queryset = User.objects.all()
                get_serializer = serializers.UserListSerializer(queryset, many=True)
            except Exception as e:
                return JsonResponse(e)
        if get_serializer.data == []:
            return JsonResponse('None')
        else:
            return JsonResponse(zlreturn(1000,get_serializer.data),safe=False)

class UserList(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.UserListAPISerializer
    # permission_classes = (IsAuthenticated,)

    def create(self, request):
        get_serializer = self.get_serializer(data=request.data)
        get_serializer.is_valid(raise_exception=True)
        post_data = get_serializer.validated_data

        if post_data:
            try:
                queryset = User.objects.filter(username=post_data["username"])
                get_serializer = serializers.UserListSerializer(queryset, many=True)
            except Exception as e:
                return JsonResponse(e)
        else:
            try:
                queryset = User.objects.all()
                get_serializer = serializers.UserListSerializer(queryset, many=True)
            except Exception as e:
                return JsonResponse(e)
        if get_serializer.data == []:
            return JsonResponse('None')
        else:
            return JsonResponse(get_serializer.data,safe=False)
