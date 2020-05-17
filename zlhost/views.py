#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
'''


from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import InfoList

from utils.return_code import zlreturn

from rest_framework.permissions import IsAuthenticated #, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins

from . import serializers

class HostList(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.HostListAPISerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        get_serializer = self.get_serializer(data=request.data)
        get_serializer.is_valid(raise_exception=True)
        post_data = get_serializer.validated_data

        if post_data:
            try:
                queryset = InfoList.objects.filter(ip=post_data["ip"])
                get_serializer = serializers.HostListDBSerializer(queryset, many=True)
            except Exception as e:
                return JsonResponse(zlreturn(1002,e))
        else:
            try:
                queryset = InfoList.objects.all()
                get_serializer = serializers.HostListDBSerializer(queryset, many=True)
            except Exception as e:
                return JsonResponse(e)
        if get_serializer.data == []:
            return JsonResponse(zlreturn(1003,'None'))
        else:
            return JsonResponse(zlreturn(1000,get_serializer.data),safe=False)
