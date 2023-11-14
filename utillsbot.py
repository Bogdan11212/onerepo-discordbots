import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# реакция при получении определенного сообщения
@bot.event
async def on_message(message):
    if message.channel.id == YOUR_CHANNEL_ID:
        await message.add_reaction(YOUR_REACTION)

# автоматически создаём ветку на каждое сообщение
@bot.event
async def on_message(message):
    channel = await message.guild.create_text_channel(message.content)

# создание приватного голосового канала в определенной категории
@bot.command()
async def create_voice_channel(ctx, category_id):
    category = disnake.utils.get(ctx.guild.categories, id=int(category_id))
    await ctx.guild.create_voice_channel(name='Private Channel', category=category)

# статус "made by frostout"
@bot.event
async def on_ready():
	bot.activity = disnake.Game(name="made by frostout")

# отправка содержания личного сообщения в определенный канал
@bot.event
async def on_message(message):
    if isinstance(message.channel, disnake.DMChannel):
        channel = bot.get_channel(YOUR_CHANNEL_ID)
        await channel.send(message.content)


bot.run('твой_токен_бота')
  