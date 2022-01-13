from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib
import discord
from discord.ext import commands

class Image(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("Moderator")
    async def picsearch(self, ctx, *, arg):
        options = Options()
        options.headless = True
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

        browser.get('https://www.google.com/imghp?hl=en')
        searchbar = browser.find_element(By.XPATH, '//*[@id="sbtc"]/div/div[2]/input')
        searchbar.send_keys(arg)
        searchbar.send_keys(Keys.RETURN)

        image = browser.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute('src')
        urllib.request.urlretrieve(image, 'SEARCH_IMG.png')
        browser.quit()

        await ctx.send("Here is the first image that comes up:", file=discord.File('SEARCH_IMG.png'))

def setup(client):
    client.add_cog(Image(client))
