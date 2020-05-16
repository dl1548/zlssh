#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   serializer.py
'''



from rest_framework import serializers
from .models import Record


class SSHLoginSerializer(serializers.Serializer):
    pass


class TerminalHistorySerializer(serializers.Serializer):
    pass

# 数据库取值 序列化
class FetchZiliDataDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'