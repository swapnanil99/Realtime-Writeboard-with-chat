from django.urls import re_path
from .consumers import someconsumer

websocket_urlpatterns = [
    re_path(r"ws/whiteboard/$", someconsumer.as_asgi()),
]
