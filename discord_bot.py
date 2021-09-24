import os
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')
NAME = os.getenv('NAME')


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == NAME, client.guilds)
    print(guild.name)
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    # for member in guild.members:
    #     if member.name == 'Ryzon' or member.name == 'Kanelao':
    #         await member.create_dm()
    #         await member.dm_channel.send(f'WTF {member.name}??? Que andas a fazer da vida????')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send('Hello Manel')


client.run(TOKEN)
