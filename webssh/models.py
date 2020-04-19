from django.db import models

# Create your models here.


class Record(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # host = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    host = models.CharField(max_length=128,verbose_name='主机')
    user = models.CharField(max_length=128,verbose_name='用户')
    filename = models.CharField(max_length=128, verbose_name='录像文件名称')

    def __str__(self):
        return self.host