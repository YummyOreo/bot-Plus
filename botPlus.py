import discord
from discord.ext import commands
import color
import time
import os

class bot:
	def __init__(self, settings: {}):
		self.bot = '';
		try:
			self.logging = settings['logging']
		except:
			self.logging = "advanced"

		try:
			self.prefix = settings['prefix']
		except:
			self.prefix = "!"
			print("Error, you need to define the prefix, it has been set to \"!\"")

	def make(self):
		self.bot = commands.Bot(command_prefix=self.prefix)
		if self.logging == 'advanced':
			print(color.green(f"[{time.asctime(time.localtime(time.time()))}]"), f"\032 Bot made with prefix [{self.prefix}]")
		else if self.logging == 'normal':
			print(f"[{time.asctime(time.localtime(time.time()))}]", f"\032 Bot made with prefix [{self.prefix}]")
		else:
			pass
		return self.bot;

	def run(self, token):
		@self.bot.event
		async def on_ready():
			if self.logging == 'advanced':
				print(color.green(f"[{time.asctime(time.localtime(time.time()))}]"), f"\032 Bot online.")
			else if self.logging == 'normal':
				print(f"[{time.asctime(time.localtime(time.time()))}]", f"\032 Bot online.")
			else:
				pass
			self.bot.remove_command("help") 
			return

		self.bot.run(token)


