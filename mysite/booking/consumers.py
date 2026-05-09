import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class TimerConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.timer_running = False
        self.current_time = 0


    async def disconnect(self, code):
        self.timer_running = False


    async def receive(self, text_data):
        data = json.loads(text_data)

        if data.get("action") =="start" and data.get("time") is not None:
            self.timer_running = True
            self.current_time = int(data["time"])
            asyncio.create_task(self.start_countdown())

        elif data.get("action") == "stop":
            self.timer_running = False
            await self.send(text_data=json.dumps({
                "massage": "таймер остановлен",
                "time": self.current_time
            }))

    async def start_countdown(self):
        while self.timer_running and self.current_time > 0:
            await self.send(text_data=json.dumps({
                "time": self.current_time
            }))
            self.current_time -= 1
            await asyncio.sleep(1)

        if self.timer_running and self.current_time ==0:
            await self.send(text_data=json.dumps({
                "massage": "время вышло!",
                "time": 0
            }))
            self.timer_running = False