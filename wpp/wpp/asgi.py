import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import wpp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wpp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            wpp.routing.websocket_urlpatterns
        )
    ),
})
