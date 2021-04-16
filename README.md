<h1 align="center">Bot Plus</h1>
<h3 align="center"><a href="https://pypi.org/project/botPlus/">Website</a></h3>


--- 

## Install:
To intall this package:
```console
$ pip install botPlus==1.0.0
```

## Set Up a simple bot:
```py
import discord
from discord.ext import commands
import botPlus

# Makes the bot 
client = botPlus.bot({'logging': 'advanced', "prefix": "!"})
bot = client.make()

# A command
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

# Runs the bot
client.run('')
```

## Docs:
Coming Soon