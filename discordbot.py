from discord.ext import commands
import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(685797761290993681)
    await channel.send('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        await message.channel.send('にゃーん')

client.run(TOKEN)
