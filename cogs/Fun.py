import discord, requests, random, time
from discord.ext import commands
from discord.ext.commands.context import Context

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    #autoreply
    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if "dok" in message.content.lower():
            await message.channel.send("kopit")

        elif "mangsut" in message.content.lower():
            await message.channel.send("iyh")

        elif "halo" in message.content.lower():
            if message.author != self.client.user:
                await message.channel.send("hai")

        elif "hai" in message.content.lower():
            if message.author != self.client.user:
                await message.channel.send("halo")

        elif "assalaamualaikum" in message.content.lower():
            await message.channel.send("Waalaikumussalaam")

        elif "samlekom" in message.content.lower():
            await message.channel.send("komsalam")

        elif "sange" in message.content.lower():
            await message.channel.send("hayoo ngapain nyentuh2 kemaluan?")

    #wangy generator
    @commands.command(name="wangytext", description="Membuat teks WANGY WANGY", aliases=["wangy"])
    async def wangytext(self, ctx:Context, obyek:str=None):
        if not obyek:
            return await ctx.send("Tuliskan objek yang ingin digunakan dalam teks.")
        
        embed = discord.Embed(
            title = "Wangy Generator",
            description = f"{obyek.upper()}........... {obyek.upper()} {obyek.upper()} {obyek.upper()} AAAAAAAAAAAAAAAAAGH AAAAAAAAAAAAAAAAAAAAAAAGH :heart: :heart: :heart: :heart: WANGI WANGI WANGI WANGI HU HA HU HA HU HA, aaaah baunya {obyek.lower()} wangi aku mau nyiumin aroma wanginya {obyek.lower()} AAAAAAAAH rambutnya.... aaah rambutnya juga pengen aku elus-elus ~~~ AAAAAH {obyek.lower()} keluar pertama kali juga manis :heart: :heart: :heart: dia pake baju itu juga manis banget AAAAAAAAH {obyek.upper()} LUCCUUUUUUUUUUUUUUU............ GUA BAKAL BAKAR DUIT 12 JUTA RUPIAH BUAT {obyek.upper()} AAAAAAAAAAAAAAAAAAAAAAAAAAAAAGH apa ? {obyek.capitalize()} itu gak nyata ? Cuma karakter 2 dimensi katamu ? nggak, ngak ngak ngak ngak NGAAAAAAAAK GUA GAK PERCAYA ITU DIA NYATA NGAAAAAAAAAAAAAAAAAK PEDULI BANGSAAAAAT !! GUA GAK PEDULI SAMA KENYATAAN POKOKNYA GAK PEDULI. {obyek.capitalize()} ngeliat gw ... {obyek.capitalize()} di HP ngeliatin gw {obyek.capitalize()}... kamu percaya sama aku ? aaaaaaaaaaah syukur {obyek.capitalize()} gak malu merelakan aku aaaaaah :heart: :heart: :heart: YEAAAAAAAAAAAH GUA MASIH PUNYA {obyek.upper()}, SENDIRI PUN NGGAK MASALAH AAAAAAAAAAAAAAH, KIRIMKANLAH CINTAKU PADA {obyek.upper()} KIRIMKAN KE- AAAAAAAAH",
            color = ctx.guild.me.color
        )
        await ctx.send(embed=embed)
        
        
    @commands.command(name="wangytexten", description="Create a WANGY WANGY text", aliases=["wangyen"])
    async def wangytext(self, ctx:Context, obyek:str=None):
        if not obyek:
            return await ctx.send("Please write who you want to add on text.")
        
        embed = discord.Embed(
            title = "Wangy Generator",
            description = f"{obyek.lower()}! {obyek.lower()} {obyek.lower()} {obyek.lower()}AAaaaaAAAaaAAa!!! :heart: :heart: :heart: :heart: UhUUUHHHHhhHHH! Unh! Uhhhhhh! {obyek.upper()} {obyek.upper()} {obyek.upper()}AaaaAAAuuUUUuh!!! Ah-Kunkakunka! Kunkakunka! Suu-HA! Suu-HA! Suu-HA! SUU-HAaa! {obyek.lower()} smells so good! Nyunhahahuh! Ahun! I want to smell the smooth hair of {obyek.lower()}! Kun-kun! Ahh! No! I want to pat her head! Mofmof-mofmof-mofmof-mofmof! :heart: :heart: :heart:",
            color = ctx.guild.me.color
        )
        await ctx.send(embed=embed)
    
    #Say
    @commands.command()
    async def say(self, ctx, *, kalimat):
        await ctx.message.delete()
        await ctx.send(kalimat)
    
    #Secret
    @commands.command(aliases=['secret', 'what', 'rickroll'])
    async def about(self, ctx:Context):
        embed = discord.Embed(
            title = "Here's your daily mood",
            color = ctx.guild.me.color
        )
        embed.add_field(
            name="⠀",
            value="[Click Here](https://youtu.be/dQw4w9WgXcQ)
            inline=False
        )

def setup(client):
    client.add_cog(Fun(client))
