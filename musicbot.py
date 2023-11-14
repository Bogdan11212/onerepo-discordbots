# Here is a basic outline for a Discord music bot that can play music and search YouTube

import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice or not voice.is_connected():
        await channel.connect()
    else:
        if voice.is_playing():
            voice.stop()
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice.play(discord.FFmpegPCMAudio(source=URL, executable="ffmpeg"))

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.stop()
        await voice.disconnect()

bot.run('YOUR_BOT_TOKEN')