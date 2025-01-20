# djangochat/asgi.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from room.routing import websocket_urlpatterns  # Adjust if your routing is in a different appp

# Set the default settings module for the 'django' program.

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
