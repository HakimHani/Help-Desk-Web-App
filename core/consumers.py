
# chat/consumers.py

import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer 
from channels.db import database_sync_to_async
# from core.models import Thread, ChatMessage

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from core.models import Document
from core.forms import DocumentForm

class ChatConsumer(AsyncConsumer):

    async def connect(self, event):
        user_id = self.scope["session"]["_auth_user_id"]
        self.group_name = "{}".format(user_id)
        # Join room group

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.send({
            "type": "webseocket.accept"
        })

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None,bytes_data = None):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'recieve_group_message',
                'message': message
            }
        )

    async def recieve_group_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(json.dumps({
            'message': message
        }))
    