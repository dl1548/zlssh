#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
'''


from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from django.contrib.auth.models import User


from rest_framework.permissions import IsAuthenticated #, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
from . import serializers

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
