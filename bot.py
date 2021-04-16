import discord
from discord.ext import commands
import botPlus

client = botPlus.bot({'logging': 'advanced', "prefix": "!"})
bot = client.make()
print(bot)
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

client.run('ODMxMzE2MzQ1Mjg2Njg4NzY4.YHTdrQ.-z4PLHrjbUW4pB0XGTD9s1LTxWg')
