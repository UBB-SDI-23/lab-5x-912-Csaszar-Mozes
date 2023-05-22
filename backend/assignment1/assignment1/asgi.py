import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment1.settings')

assignment1 = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # new
    'websocket': URLRouter(
        websocket_urlpatterns),
})