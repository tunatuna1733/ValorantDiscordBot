import discord
import os
from dotenv import load_dotenv

from utils.fetch import Fetch

load_dotenv(override=True)

TOKEN = os.environ['DISCORD_TOKEN']
bot = discord.Bot(intents=discord.Intents.all())

fetch = Fetch()

@bot.event
async def on_ready():
    print('Ready')
    systemLogChannel = bot.get_channel(00000)
    await fetch.updateRiotId(channel=systemLogChannel)
    #await bot.change_presence(activity=discord.Game('VALORANT'), status=discord.Status.online)

if __name__ == '__main__':
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')
    bot.run(TOKEN)