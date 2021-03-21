import discord
import asyncio

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
		date_channel = self.get_channel(823000204810125352)
		time_channel = self.get_channel(822987807743016970)
		time = datetime.utcnow()

		while True:
			await date_channel.edit(name=f'Date: {time.strftime("%d/%m")}')
			await time_channel.edit(name=f'Time: {time.strftime("%H:%M")}')
			await asyncio.sleep(60)

client = MyClient()
client.run('ODIyOTgzMzgwNTA0Njc0MzY1.YFaNAA.MhsrRzbnebCgXC9v1eqW9DHYd5s')