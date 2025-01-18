# room/routing.py

from django.urls import re_path
from . import consumers

# Define the WebSocket URL pattern
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),  # Match URL and pass room_name to consumer
]
