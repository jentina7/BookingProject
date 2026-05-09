from django.urls import path
from .consumers import TimerConsumers

websocket_urlpatterns = [
    path("ws/timer/", TimerConsumers.as_asgi()),
]