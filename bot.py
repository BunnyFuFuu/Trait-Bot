import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='$')

@bot.command(name='hi')
async def hi(ctx):
    response = 'Hello world'
    await ctx.send(response)

@bot.command(name='randtrait')
async def random_trait(ctx):
    opened = open("traits.txt", "r")
    traits = [line for line in opened]
    numlines = len(traits)
    response = traits[random.randint(0, numlines-1)]
    await ctx.send(response)

@bot.command(name='find')
async def search(ctx, arg):
    opened = open("traits.txt", "r")
    traits = [line for line in opened]
    for line in traits:
        if arg in line:
            await ctx.send(line)
            break
    opened.close()

# TODO: Have the sorting algorithm ignore the header
@bot.command(name='insert')
async def insert(ctx, arg, arg1):
    opened = open("traits.txt", "r")
    traits = opened.readlines()
    opened.close()
    builder = '** ' + arg + ' ** - '+ arg1 + '\n'
    traits.append(builder)
    traits = sorted(traits)
    opened = open("traits.txt", "w")
    modified = "".join(traits)
    opened.write(modified)
    opened.close()

@bot.command(name='delete')
async def delete(ctx, arg):
    opened = open("traits.txt", "r")
    traits = opened.readlines()
    opened.close()
    modified = []
    for line in traits:
        if arg not in line:
            modified.append(line)
    modified = "".join(modified)
    opened = open("traits.txt", "w")
    opened.write(modified)
    opened.close()
    await ctx.send("Successfully deleted.")
@bot.command(name='commands')
async def commands(ctx):
    message = 'Type ```$randtrait``` to get a random trait from our list,\n ```$find "Name of trait in quotes" ``` to find a trait in the list and have me define it, \n ```$insert "Name of trait in quotes" "Definition of trait in quotes"``` to insert a new trait and definition in our traits file, ```$delete "Name of trait in quotes" ``` to delete a trait if it is in our traits file'
    await ctx.send(message)

bot.run(TOKEN)