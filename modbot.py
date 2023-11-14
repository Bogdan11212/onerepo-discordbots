import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: disnake.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: disnake.Member):
    # mute logic here

@bot.command()
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member: disnake.Member):
    # unmute logic here

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: disnake.TextChannel):
    # lock channel logic here

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: disnake.TextChannel):
    # unlock channel logic here

bot.run('твой_токен_бота')