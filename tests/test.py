import discord
from discord.ext import commands
import testMod

client = testMod.bot({'logging': 'advanced', "prefix": "!"})
bot = client.make()
print(bot)
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

print(client.getAll())