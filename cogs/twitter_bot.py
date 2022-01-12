import tweepy
import os
from discord.ext import commands

authenticator = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_KEY_SEC'))
authenticator.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SEC'))
api = tweepy.API(authenticator, wait_on_rate_limit=True)

class Twitter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tweet(self, ctx, arg):
        api.update_status(arg)
        await ctx.send("Tweet has been sent!\n https://twitter.com/hell0hell0hello")

def setup(client):
    client.add_cog(Twitter(client))