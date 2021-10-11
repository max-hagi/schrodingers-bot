import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return
        if "marko" in str.lower(message.content):
            await message.reply(f"Hey {message.author}, I think you meant Anne Frank!", mention_author=True)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Greetings human")

def setup(client):
    client.add_cog(General(client))