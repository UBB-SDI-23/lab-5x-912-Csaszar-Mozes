from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        await super().disconnect(code)

    async def echo_message(self, message):  # new
        await self.send_json({
            'type': message.get('type'),
            'nickname': message.get('nickname'),
            'data': message.get('data'),
        })

    # Type: type = message, nickname = Something, data=Something
    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        print(content)
        if message_type == 'chat_message':
            await self.send_json({
                'type': message_type,
                'nickname': content.get('nickname'),
                'data': content.get('data'),
            })
