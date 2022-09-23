import discord, os
from discord.ext import commands, tasks
from itertools import cycle
import asyncio


TOKEN = #Tulis Token Anda disini
#===============================================================================================

#setel prefix + bikin variabel client
client = commands.Bot(command_prefix=["c.", "C.", "cel ", "Cel ", "Cecillia ", "cecillia ","Cecillia", "cecillia" ], case_insensitive=True, intents=discord.Intents.all())

#hilangkan help bawaan
client.remove_command('help')

#===============================================================================================

#daftarin cog
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

#===============================================================================================

#tulisan siap pada terminal dan status yg berganti2
@client.event
async def on_ready():
    change_status.start()
    print('main.py, siap sedia!')
    
    channel = client.get_channel(791704672351813634)
    await channel.send(f"{client.user} siap menerima perintah, Senpai!")
    
#===============================================================================================

#isi status
status = cycle([
    'c.help',
    "Join Chrono Curses!",
    "With you~",
    " ",
    'Don\'t forget to wash your hand',
    'Keep your distance with another people',
    'avoid too much contact with random people',
    'Stay safe',
    "Enjoy your life whatever happened",
    "Don't worry, Be Happy!"
])

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#===============================================================================================

#nyalakan bot. 
async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)

asyncio.run(main())
