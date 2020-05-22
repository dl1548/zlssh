from channels.generic.websocket import WebsocketConsumer
from webssh.ssh_conn import SSH
from django.http.request import QueryDict
from django.utils.six import StringIO
from zlssh.settings import TMP_DIR
from zlssh.settings import RECORD_DIR
from .models import Record
from webssh.ssh_tools import record_log
import os
import time
import json
import base64


class WebSSH(WebsocketConsumer):
    message = {'status': 0, 'message': None}
    """
    status:
        0: ssh 连接正常, websocket 正常
        1: 发生未知错误, 关闭 ssh 和 websocket 连接

    message:
        status 为 1 时, message 为具体的错误信息
        status 为 0 时, message 为 ssh 返回的数据, 前端页面将获取 ssh 返回的数据并写入终端页面
    """
    # # 初始化 Asciinema 文件名 (主机+用户+ 时间)
    # def __init__(self, host, user, websocket):
    #     self.host = '127.0.0.1'
    #     self.user = 'zilitest'
    #     self.time = time.time()
    #     self.filename = '%s.%s.%d.cast' % (host, user, self.time)

    def connect(self):
        """
        打开 websocket 连接, 通过前端传入的参数尝试连接 ssh 主机
        :return:
        """
        self.accept()
        query_string = self.scope.get('query_string')
        ssh_args = QueryDict(query_string=query_string, encoding='utf-8')

        width = ssh_args.get('width')
        height = ssh_args.get('height')
        port = ssh_args.get('port')

        width = int(width)
        height = int(height)
        port = int(port)

        auth = ssh_args.get('auth')
        ssh_key_name = ssh_args.get('ssh_key')
        passwd = ssh_args.get('password')

        host = ssh_args.get('host')
        user = ssh_args.get('user')

        connect_time = time.time()
        filename = '%s.%s.%d.cast' % (host, user, connect_time)  # 文件名

        # 构建录像文件header
        record_log(
            type = 'header', 
            data = {
            "version": 2,
            "width": width,
            "height": height,
            "timestamp": connect_time,
            "env": {
                "SHELL": "/bin/bash",
                "TERM": 'xterm-256color'
            },
            "title": "zili-webssh"
            },
            connect_time = connect_time,
            host = host,
            user = user,
            filename = filename
        )

        if passwd:
            passwd = base64.b64decode(passwd).decode('utf-8')
        else:
            passwd = None

        self.ssh = SSH(websocker=self, message=self.message)

        ssh_connect_dict = {
            'host': host,
            'user': user,
            'port': port,
            'timeout': 30,
            'pty_width': width,
            'pty_height': height,
            'password': passwd,
            'filename':filename,
            'connect_time':connect_time
        }

        if auth == 'key':
            ssh_key_file = os.path.join(TMP_DIR, ssh_key_name)
            with open(ssh_key_file, 'r') as f:
                ssh_key = f.read()

            string_io = StringIO()
            string_io.write(ssh_key)
            string_io.flush()
            string_io.seek(0)
            ssh_connect_dict['ssh_key'] = string_io

            os.remove(ssh_key_file)


        self.ssh.connect(**ssh_connect_dict)

    def disconnect(self, close_code):
        try:
            self.ssh.close()
        except:
            pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if type(data) == dict:
            status = data['status']
            if status == 0:
                data = data['data']
                self.ssh.shell(data)
            else:
                cols = data['cols']
                rows = data['rows']
                self.ssh.resize_pty(cols=cols, rows=rows)
        