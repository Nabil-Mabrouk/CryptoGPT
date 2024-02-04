# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_news_update(self, event):
        message = event['message']

        # Send news update to the WebSocket
        await self.send(text_data=json.dumps({'message': message}))
