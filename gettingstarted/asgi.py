import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import hello.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gettingstarted.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            hello.routing.websocket_urlpatterns
        )
    ),
})