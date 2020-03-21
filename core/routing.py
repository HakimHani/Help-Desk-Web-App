from core import consumers
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack




channels_routing = [
            url(r"^ws/core/$", consumers.ChatConsumer.connect),
            url(r"^ws/core/$", consumers.ChatConsumer.disconnect),
            url(r"^ws/core/$", consumers.ChatConsumer.receive),
            url(r"^ws/core/$", consumers.ChatConsumer.recieve_group_message),
            # url(r"^ws/core/$", consumers.ChatConsumer.model_form_upload),
            
]
    



