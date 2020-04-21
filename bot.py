import os
import random
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
        await ctx.send(" ".join(row))

await ctx.send("Welcome to Battleship! Sink Your Enemy Ships Before They Sink Yours!")
await ctx.send(print_grid(grid))

@bot.command(name="random_row", help="picks a random row")
async def random_row(grid):
        await ctx.send(random.randint(1, 7))

@bot.command(name="random_col", help="picks a random col")
async def random_col(grid):
        await ctx.send(random.randint(1, 7))

battle_row = random_row(grid)
battle_col = random_col(grid)

for turn in range(6):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    if guess_row == battle_row and guess_col == battle_col:
        await ctx.send("Ahhhh you got me, darn it😞! Good game.")
        break
    if turn == 5:
            await ctx.send("aHaH, you lost😂😂😂!! But good game.")
            await ctx.send("My ship was here: [" + str(battle_row) + "][" + str(battle_col) + "]")
        else:
              if (int(guess_row) < 1 or int(guess_row) >= 7) or (int(guess_col) < 1 or int(guess_col) >= 7):
                await ctx.send("Dummy, that's not even in the ocean😋")
              elif(grid[int(guess_row)][int(guess_col)] == "X"):
                await ctx.send("Sillyyyyy🙈, try again.")
              await ctx.send(turn + 1)
              await ctx.send(print_grid(grid))



bot.run(TOKEN)
