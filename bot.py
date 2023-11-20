import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_GUILD_CHANNEL')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!') 

@bot.command(name='hello')
async def hello(ctx):
    response = "Hello World!"
    await ctx.send(response)

bot.run(TOKEN)