import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix=["c.", "C."], case_insensitive=True, intents=discord.Intents.all())

for namafile in os.listdir('./cogs'):
    if namafile.endswith('.py'):
        client.load_extension(f'cogs.{namafile[:-3]}')
        print(f"{namafile} dimuat")
  
client.run("ODY0MDQzNzIwMjk3OTM4OTQ2.YOvtbA.Aj9A1NGbr33GVvPqWPiUe2Qkioo")
