from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({
            'message': text_data
        }))
    
    async def my_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))