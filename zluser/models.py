from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=64)
    role     = models.TextField()
    add_date = models.DateTimeField('保存日期', default=timezone.now)

    def __unicode__(self):
        return self.username

