from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from webssh.ssh_tools import unique
from zlssh.settings import TMP_DIR

from rest_framework.permissions import IsAuthenticated #, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
from . import serializers


class SSHLogin(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.SSHLoginSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        """
         web shh 登录
        """
        get_serializer = self.get_serializer(data=request.data)
        get_serializer.is_valid(raise_exception=True)
        post_data = get_serializer.validated_data

        pass

        # if post_data["task_id"]:
        #     try:
        #         res = AsyncResult(post_data["task_id"])
        #         if res.ready():  # 检查指定任务是否已经完成
        #             res = res.result  # res.result为任务函数的返回值 即任务结果
        #             jklog.debug(res)
        #             if res['code'] == 200:
        #                 return JsonResponse(jkreturn(200, res['data']))
        #             return JsonResponse(res)
        #     except Exception as e:
        #         jklog.error(e)
        #         return JsonResponse(jkreturn(1002, data=e))
        # else:
        #     return JsonResponse(jkreturn(1005, data=[]))


class TerminalHistory(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.TerminalHistorySerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        """
        web shh 回放
        """
        get_serializer = self.get_serializer(data=request.data)
        get_serializer.is_valid(raise_exception=True)
        post_data = get_serializer.validated_data

        pass


def index(request):
    return render(request, 'webssh.html')

def history(request):
    return render(request, 'record.html')

def upload_ssh_key(request):
    if request.method == 'POST':
        pkey = request.FILES.get('pkey')
        ssh_key = pkey.read().decode('utf-8')

        while True:
            filename = unique()
            ssh_key_path = os.path.join(TMP_DIR, filename)
            if not os.path.isfile(ssh_key_path):
                with open(ssh_key_path, 'w') as f:
                    f.write(ssh_key)
                break
            else:
                continue

        return HttpResponse(filename)
