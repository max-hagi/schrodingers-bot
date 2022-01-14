import discord
from discord.ext import commands, tasks
import os

client = commands.Bot(command_prefix='!')
intents = discord.Intents.all()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("HuniePop"))
    print("My pronouns are bit/bot")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    else:
        print(f'Unable to load {filename[:-3]}')

client.run(os.getenv('TOKEN'))
