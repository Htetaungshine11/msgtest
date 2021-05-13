from django.urls import path
from .consumer import web
app = [
    path("room/<str:name>/",web.as_asgi()),
]