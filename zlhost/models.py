#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
'''

from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class InfoList(models.Model):
    ip         = models.CharField(max_length=64,unique=True)
    port       = models.CharField(max_length=5)
    username   = models.CharField(max_length=64)
    login_type = models.CharField(max_length=64)  # passwd /  key
    key_file   = models.CharField(max_length=64)
    password   = models.CharField(max_length=64)
    add_date   = models.DateTimeField('保存日期', default=timezone.now)

    def __unicode__(self):
        return self.ip

