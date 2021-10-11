import discord
from discord.ext import commands

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Missing required information dipshit.", mention_author=True)
        if isinstance(error, commands.MissingRole):
            await ctx.reply("You lack the knowledge to do that.", mention_author=True)

def setup(client):
    client.add_cog(Errors(client))