import json
from channels.generic.websocket import AsyncWebsocketConsumer

class someconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Assign the room name (all users join same "boardroom")
        self.room_name = "boardroom"

        # Add this WebSocket connection to the group
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        # Accept the connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove connection from group when user leaves
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        # Receive message from a client
        data = json.loads(text_data)

        # Check the type of message
        msg_type = data.get("type")

        if msg_type == "draw":
            # Broadcast drawing data to everyone in the group
            await self.channel_layer.group_send(
                self.room_name,
                {
                    "type": "broadcast_draw",
                    "message": data
                }
            )
        elif msg_type == "chat":
            # Broadcast chat message to everyone in the group
            await self.channel_layer.group_send(
                self.room_name,
                {
                    "type": "broadcast_chat",
                    "message": data
                }
            )

    # Called when a draw message is broadcasted
    async def broadcast_draw(self, event):
        await self.send(text_data=json.dumps(event["message"]))

    # Called when a chat message is broadcasted
    async def broadcast_chat(self, event):
        await self.send(text_data=json.dumps(event["message"]))
