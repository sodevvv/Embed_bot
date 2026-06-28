import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
import json
load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


async def load_components():
    await bot.load_extension("components.embed")
@bot.event
async def on_ready():
    await load_components()
    synced = await bot.tree.sync()
    

bot.run(os.getenv("TOKEN"))
