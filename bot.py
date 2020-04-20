import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")

grid = []

for y in range(1, 7):
    grid.append(["X"] * 6)

@bot.command(name="print_grid", help="prints out grid")
async def print_grid(grid, ctx):
    for row in grid:
        print(" ".join(row))

await ctx.send("Welcome to Battleship! Sink Your Enemy Ships Before They Sink Yours!")
await ctx.send(print_grid(grid))



bot.run(TOKEN)
