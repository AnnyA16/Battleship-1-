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

for turn in range(6):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    if guess_row == battle_row and guess_col == battle_col:
      print ("Ahhhh you got me, darn it😞! Good game.")
      break
    if turn == 5:
            print ("aHaH, you lost😂😂😂!! But good game.")
            print ("My ship was here: [" + str(battle_row) + "][" + str(battle_col) + "]")
    else:
            if (int(guess_row) < 1 or int(guess_row) >= 7) or (int(guess_col) < 1 or int(guess_col) >= 7):
                print ("Dummy, that's not even in the ocean😋")
            elif(grid[int(guess_row)][int(guess_col)] == "X"):
                print ("Sillyyyyy🙈, try again.")
            print (turn + 1)
            print_grid(grid)



bot.run(TOKEN)
