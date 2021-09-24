import os
import discord
from dotenv import load_dotenv

from discord.ext import commands
load_dotenv()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)


TOKEN = os.getenv('DISCORD_TOKEN')
NAME = os.getenv('NAME')


@bot.command(name='test', help='Responds with a Test Message')
async def msg(channel):
    await channel.send('Hello Manel')


@bot.command(name='m', help='Spams Fucking Miguel')
async def fucking_miguel(channel, number_of_times: int):
    for _ in range(number_of_times):
        await channel.send('Fucking Miguel')


@bot.command(name='p', help='Plays Music from the given url')
async def play(channel, url: str):

    channel = channel.message.author.voice.channel
    voice_channel = discord.utils.get(
        channel.guild.voice_channels, name=channel.name)
    voice_client = discord.utils.get(bot.voice_clients, guild=channel.guild)

    if voice_client == None:
        await voice_channel.connect()
    else:
        await voice_client.move_to(channel)


@bot.command(name='l', help='Stops Music bot')
async def leave(channel):

    for voice_channel in bot.voice_clients:
        if voice_channel.guild == channel.guild:
            await voice_channel.disconnect()


@bot.command(name='pa', help='Pauses Music bot')
async def pause(channel):
    voice_client = discord.utils.get(bot.voice_clients, guild=channel.guild)
    if voice_client.is_playing():
        voice_client.pause()
    else:
        await channel.send('Nothing is Playing Manel')


@bot.command(name='r', help='Resumes Music bot')
async def resume(channel):
    voice_client = discord.utils.get(bot.voice_clients, guild=channel.guild)
    if voice_client.is_paused():
        voice_client.resume()
    else:
        await channel.send("It's already playing Manel")

@bot.command(name='s', help='Stops Music bot')
async def stop(channel):
    voice_client = discord.utils.get(bot.voice_clients, guild=channel.guild)
    voice_client.stop()

bot.run(TOKEN)
