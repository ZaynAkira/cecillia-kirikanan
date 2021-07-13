import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix=["c.", "C."], case_insensitive=True, intents=discord.Intents.all())

for namafile in os.listdir('./cogs'):
    if namafile.endswith('.py'):
        client.load_extension(f'cogs.{namafile[:-3]}')
        print(f"{namafile} dimuat")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('c.help'))
    print(f"\n{client.user} sudah siap.")

    channel = client.get_channel(847885141019983962)
    await channel.send(f"**{client.user}** telah diaktifkan kembali setelah diperbaiki. Sistem sudah berjalan normal kembali~! yaay! <:1_CelLovely:797873134375796776>")

    channel = client.get_channel(858697952436158464)
    await channel.send(f"**{client.user}** telah diaktifkan kembali setelah diperbaiki. Sistem sudah berjalan normal kembali~! yaay! <:1_CelLovely:797873134375796776>")
   
client.run(os.environ["ODY0MDQzNzIwMjk3OTM4OTQ2.YOvtbA.gEYRroII0NujJ8dW0cNVXSBe3Vc"])
