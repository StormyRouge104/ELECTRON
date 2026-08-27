import asyncio
import os
from dotenv import load_dotenv
import discord
from datetime import datetime
from discord.ext import commands, tasks
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
client = commands.Bot(command_prefix = "$" , intents=intents) ## префикс обязательно оставлять а то питон трахнет
async def load_comms(): # команды, async нужон шобы бот не зависал пока ждёт ответа от одного чувака
    await client.load_extension("ping")
    await client.load_extension("pic")
    await client.load_extension("help")
    await client.load_extension("vote")
    await client.load_extension("votestage1")
    await client.tree.sync()
client.setup_hook = load_comms

ostalos = datetime(2026, 12, 16) # отсчёт до 16 декабря

@tasks.loop(hours=12)
async def otchet():
    days_left = (ostalos.date() - datetime.now().date()).days
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=f"104 AWARDS через {days_left} дней(-я)"
    )
    await client.change_presence(activity=activity)
@client.event
async def on_ready():
    otchet.start()
client.run(os.getenv("DISCORD_TOKEN"))
