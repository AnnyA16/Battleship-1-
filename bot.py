import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix='!')


@client.listen()
async def on_ready():
    print('Bot loaded and ready!')

@client.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")

grid = []

for y in range(1, 7):
    grid.append(["X"] * 6)

@client.command(name="print_grid", help="prints out grid")
async def print_grid(grid):
    for row in grid:
        await (" ".join(row))

await ("Welcome to Battleship! Sink Your Enemy Ships Before They Sink Yours!")
print_grid(grid)

@client.command(name="random_row", help="picks a random row")
async def random_row(grid):
        await (random.randint(1, 7))

@client.command(name="random_col", help="picks a random col")
async def random_col(grid):
        await (random.randint(1, 7))

battle_row = random_row(grid)
battle_col = random_col(grid)

for turn in range(6):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    if guess_row == battle_row and guess_col == battle_col:
        await ("Ahhhh you got me, darn it😞! Good game.")
        break
    if turn == 5:
            await ("aHaH, you lost😂😂😂!! But good game.")
            await ("My ship was here: [" + str(battle_row) + "][" + str(battle_col) + "]")
    else:
              if (int(guess_row) < 1 or int(guess_row) >= 7) or (int(guess_col) < 1 or int(guess_col) >= 7):
                await ("Dummy, that's not even in the ocean😋")
              elif(grid[int(guess_row)][int(guess_col)] == "X"):
                await ("Sillyyyyy🙈, try again.")
              await (turn + 1)
              print_grid(grid)



client.run(TOKEN)




bot.run(TOKEN)
