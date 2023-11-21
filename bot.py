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

@bot.command(name="left")
async def command(ctx):
    fnafbot.look_left()

@bot.command(name="right")
async def command(ctx):
    fnafbot.look_right()

@bot.command(name="ldoor")
async def command(ctx):
    fnafbot.left_door()

@bot.command(name="rdoor")
async def command(ctx):
    fnafbot.right_door()

@bot.command(name="llight")
async def command(ctx):
    fnafbot.left_light()

@bot.command(name="rlight")
async def command(ctx):
    fnafbot.right_light()

@bot.command(name="camera")
async def command(ctx):
    fnafbot.toggleCam()

@bot.command(name="1a")
async def command(ctx):
    fnafbot.one_a()

@bot.command(name="1b")
async def command(ctx):
    fnafbot.one_b()

@bot.command(name="1c")
async def command(ctx):
    fnafbot.one_c()

@bot.command(name="2a")
async def command(ctx):
    fnafbot.two_a()

@bot.command(name="2b")
async def command(ctx):
    fnafbot.two_b()

@bot.command(name="3")
async def command(ctx):
    fnafbot.three()

@bot.command(name="4a")
async def command(ctx):
    fnafbot.four_a()

@bot.command(name="4b")
async def command(ctx):
    fnafbot.four_b()

@bot.command(name="5")
async def command(ctx):
    fnafbot.five()

@bot.command(name="6")
async def command(ctx):
    fnafbot.six()

@bot.command(name="7")
async def command(ctx):
    fnafbot.seven()


bot.run(TOKEN)