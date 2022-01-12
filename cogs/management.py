import discord
from discord.ext import commands


class Management(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined a server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left a sever.")

    @commands.command()
    @commands.has_role("Moderator")
    async def clear(self, ctx, amount:int):
        await ctx.channel.purge(limit=amount + 1)



def setup(client):
    client.add_cog(Management(client))

