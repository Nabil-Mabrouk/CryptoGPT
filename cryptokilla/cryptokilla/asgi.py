"""
ASGI config for cryptokilla project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from landing.consumers import MyConsumer
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptokilla.settings')

#application = get_asgi_application()
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/my_endpoint/', MyConsumer.as_asgi()),
    ])
})
