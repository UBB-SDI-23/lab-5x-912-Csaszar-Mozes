from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from ..a1_api.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'api/chat/$', ChatConsumer.as_asgi()),
]