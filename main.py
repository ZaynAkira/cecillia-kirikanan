import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix=["c.", "C.", "cel ", "Cel ", "Cecillia ", "cecillia "], case_insensitive=True, intents=discord.Intents.all())

for namafile in os.listdir('./cogs'):
    if namafile.endswith('.py'):
        client.load_extension(f'cogs.{namafile[:-3]}')
        print(f"{namafile} loaded successfully")
        
@client.event
async def on_ready():
    print(f"\n{client.user} ready.")
  
client.run("tebak")
