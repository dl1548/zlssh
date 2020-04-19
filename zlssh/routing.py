from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from webssh.websocket_conn import WebSSH


from django.urls import path, re_path

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            # re_path(r'^pod/(?P<name>\w+)', SSHConsumer),
            path('webssh/', WebSSH),
        ])
    ),
})