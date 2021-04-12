import discord
import asyncio
import time
import os

from datetime import datetime
from discord.ext import tasks, commands

class MyClient(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	async def on_ready(self):
		print(f'Logged in as: {client.user.name}')
		print(f'With ID: {client.user.id}')

		await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the time"))
		await self.update_channel()

	async def update_channel(self):
		print('Starting update...')
		date_channel = self.get_channel(831255394793947237)
		time_channel = self.get_channel(831255432705343528)

		while True:
			minutes_now = datetime.utcnow().strftime("%M")
			print(f"Checking for minute: {minutes_now}")
			if minutes_now.endswith("0") or minutes_now.endswith("5"):
				break
			
			time.sleep(5)
		
		while True:
			print('Updating!')
			time_now = datetime.utcnow()
			await date_channel.edit(name=f'Date: {time_now.strftime("%d/%m")}')
			await time_channel.edit(name=f'Time: {time_now.strftime("%H:%M")}')
			time.sleep(300)

client = MyClient()
client.run(os.environ.get("BOT_TOKEN"))