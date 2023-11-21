import os
import discord
import fnafbot
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
    fnafbot.start()
    print(f'{bot.user.name} is ready to go')

@bot.command(name='hello')
async def hello(ctx):
    response = "Hello World!"
    await ctx.send(response)

@bot.command(name='mouse')
async def getPosition(ctx):
    pos = fnafbot.getMousePosition()
    response = f"x: {pos[0]}\ny: {pos[1]}"
    await ctx.send(response)

@bot.command(name="list")
async def help(ctx):
    with open("help.txt") as f:
        data = f.read()
    await ctx.send(data)

@bot.command(name="start")
async def command(ctx):
    fnafbot.start()

@bot.command(name="continue")
async def command(ctx):
    fnafbot.continue_game()

@bot.command(name="l")
async def command(ctx):
    fnafbot.look_left()

@bot.command(name="r")
async def command(ctx):
    fnafbot.look_right()

@bot.command(name="ld")
async def command(ctx):
    fnafbot.left_door()

@bot.command(name="rd")
async def command(ctx):
    fnafbot.right_door()

@bot.command(name="ll")
async def command(ctx):
    fnafbot.left_light()

@bot.command(name="rl")
async def command(ctx):
    fnafbot.right_light()

@bot.command(name="c")
async def command(ctx):
    fnafbot.toggleCam()

@bot.command(name="1a")
async def command(ctx):
    fnafbot.press("1a")

@bot.command(name="1b")
async def command(ctx):
    fnafbot.press("1b")

@bot.command(name="1c")
async def command(ctx):
    fnafbot.press("1c")

@bot.command(name="2a")
async def command(ctx):
    fnafbot.press("2a")

@bot.command(name="2b")
async def command(ctx):
    fnafbot.press("2b")

@bot.command(name="3")
async def command(ctx):
    fnafbot.press("3")

@bot.command(name="4a")
async def command(ctx):
    fnafbot.press("4a")

@bot.command(name="4b")
async def command(ctx):
    fnafbot.press("4b")

@bot.command(name="5")
async def command(ctx):
    fnafbot.press("5")

@bot.command(name="6")
async def command(ctx):
    fnafbot.press("6")

@bot.command(name="7")
async def command(ctx):
    fnafbot.press("7")

@bot.command(name="bind")
async def command(ctx, command):
    fnafbot.bind(command)


bot.run(TOKEN)