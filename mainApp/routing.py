from django.urls import re_path

from . import chatConsumer

websocket_patterns = [
    re_path(r"ws/(?P<room_name>\w+)/$", chatConsumer.ChatConsumer.as_asgi())
]