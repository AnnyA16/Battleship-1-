import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name})

@bot.command(name="random_row", help="Selects a random row")
async def random_row(grid):
    await ctx.send(random.randint(0,6))

@bot.command(name="random_col", help="Selects a random column")
async def random_col(board):
    await ctx.send(random.randint(0,6))

ship_row = random_row(grid)
print(ship_row)
ship_col = random_col(grid)
print(ship_col)
bot.run(TOKEN)
