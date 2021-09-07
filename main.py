from keep_alive import keep_alive
import discord
import os
#import requests
import json
from discord.ext.commands import Bot
#from discord.ext import commands
#import random

bot = Bot("!")

@bot.command()
async def text(ctx):
    await ctx.send("Command executed")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game('Your Mom'))

with open('user_data.json') as f:
  data = json.load(f)

print(data['123']['roblox_username'])

#bot.run(os.getenv('TOKEN'))
#keep_alive()