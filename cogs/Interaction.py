import discord, requests, random, time
from discord.ext import commands
from discord.ext.commands.context import Context

class Interaction(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    #interaksi
    @commands.command(name="hug", description="Memeluk", aliases=["peluk"])
    async def hug(self, ctx:Context, *, member:discord.Member=None):
        api = requests.get("https://some-random-api.ml/animu/hug").json()

        if not member:
            return await ctx.send("Please write who you want to hug.")

        embed = discord.Embed(
            color = ctx.guild.me.color
        )
        embed.set_image(url=api["link"])

        if member.id == ctx.author.id:
            embed.title = 'You just hugged yourself, pathetic'
        elif member.id != ctx.author.id:
            embed.title = f"{ctx.author.name} hugged {member.name}"

        await ctx.send(embed=embed)

    @commands.command(name="pat", description="Menepuk", aliases=["tepuk"])
    async def pat(self, ctx:Context, *, member:discord.Member=None):
        api = requests.get("https://some-random-api.ml/animu/pat").json()

        if not member:
            return await ctx.send("Please write who you want to pat.")

        embed = discord.Embed(
            color = ctx.guild.me.color
        )
        embed.set_image(url=api["link"])

        if member.id == ctx.author.id:
            embed.title = 'You just pat yourself? But how?'
        elif member.id != ctx.author.id:
            embed.title = f"{ctx.author.name} Pat {member.name}"

        await ctx.send(embed=embed)

    @commands.command(name="wink", description="Berkedip", aliases=["kedip"])
    async def wink(self, ctx:Context):
        api = requests.get("https://some-random-api.ml/animu/wink").json()

        embed = discord.Embed(
            title = f"{ctx.author.name} winked",
            color = ctx.guild.me.color
        )
        embed.set_image(url=api["link"])
        await ctx.send(embed=embed)

    @commands.command(name="blush", description="Nge-Blush", aliases=["blushed"])
    async def blush(self, ctx:Context, *, member:discord.Member=None):
        member = ctx.author if not member else member

        api = requests.get("https://shiro.gg/api/images/blush").json()

        embed = discord.Embed(
            title = f"{member.name} blushed",
            color = ctx.guild.me.color
        )
        embed.set_image(url=api["url"])
        await ctx.send(embed=embed)

    @commands.command(name="cry", description="Menangis", aliases=["nangis", "menangis"])
    async def cry(self, ctx:Context, *, member:discord.Member=None):
        member = ctx.author if not member else member

        api = requests.get("https://shiro.gg/api/images/cry").json()

        embed = discord.Embed(
            title = f"{member.name} just cried, what just you do?!",
            color = ctx.guild.me.color
        )
        embed.set_image(url=api["url"])
        await ctx.send(embed=embed)

    @commands.command(name="kiss", description="Mencium", aliases=["cium"])
    async def kiss(self, ctx:Context, *, member:discord.Member=None):
        if not member:
            return await ctx.send("Please write who you want to kiss. ||Imagine kissing yourself.||")

        api = requests.get("https://shiro.gg/api/images/kiss").json()

        if ctx.author.id != member.id:
            embed = discord.Embed(
                title = f"{ctx.author.name} kissed {member.name}, aww... so sweet~",
                color = ctx.guild.me.color
            )
            embed.set_image(url=api["url"])
            await ctx.send(embed=embed)
        else:
            await ctx.reply("You can't kiss yourself you know. Or try use a mirror.")

    @commands.command(name="lick", description="Menjilat", aliases=["jilat"])
    async def lick(self, ctx:Context, *, member:discord.Member=None):
        if not member:
            return await ctx.send("Please write who you want to lick. ||Imagine licking yourself.||")

        api = requests.get("https://shiro.gg/api/images/lick").json()

        if ctx.author.id != member.id:
            embed = discord.Embed(
                title = f"{ctx.author.name} lick {member.name}, ew gross",
                color = ctx.guild.me.color
            )
            embed.set_image(url=api["url"])
            await ctx.send(embed=embed)
        else:
            await ctx.reply("Licking yourself? Really?")

    @commands.command(name="nom", description="Memakan", aliases=["makan"])
    async def nom(self, ctx:Context, *, member:discord.Member=None):
        if not member:
            return await ctx.send("Please write who you want to nom. ||Imagine ate yourself.||")

        api = requests.get("https://shiro.gg/api/images/nom").json()

        if ctx.author.id != member.id:
            embed = discord.Embed(
                title = f"{ctx.author.name} nom {member.name}",
                color = ctx.guild.me.color
            )
            embed.set_image(url=api["url"])
            await ctx.send(embed=embed)
        else:
            await ctx.reply("you can't... what? Ok I need a drink now")

    @commands.command(name="poke", description="Mencolek", aliases=["colek"])
    async def poke(self, ctx:Context, *, member:discord.Member=None):
        if not member:
            return await ctx.send("Please write who you want to poke.")

        api = requests.get("https://shiro.gg/api/images/poke").json()

        if ctx.author.id != member.id:
            embed = discord.Embed(
                title = f"{ctx.author.name} poke {member.name}",
                color = ctx.guild.me.color
            )
            embed.set_image(url=api["url"])
            await ctx.send(embed=embed)
        else:
            await ctx.reply("Sorry, but you can't do this to yourself. You can, but that's not how this bot work.")

    @commands.command(name="pout", description="Mencibir", aliases=["cibir", "ngambek"])
    async def pout(self, ctx:Context, *, member:discord.Member=None):
        member = ctx.author if not member else member

        api = requests.get("https://shiro.gg/api/images/pout").json()

        embed = discord.Embed(
            title = f"{member.name} just pout, what did you do lately?",
            color = ctx.guild.me.color
        )
        embed.set_image(url=api["url"])
        await ctx.send(embed=embed)

    @commands.command(name="punch", description="Meninju", aliases=["tinju"])
    async def punch(self, ctx:Context, *, member:discord.Member=None):
        if not member:
            return await ctx.send("Please write who you want to punch. ||Imagine punching yourself. Are you even mad?||")

        api = requests.get("https://shiro.gg/api/images/punch").json()

        if ctx.author.id != member.id:
            embed = discord.Embed(
                title = f"{ctx.author.name} Meninju {member.name}",
                color = ctx.guild.me.color
            )
            embed.set_image(url=api["url"])
            await ctx.send(embed=embed)
        else:
            await ctx.reply("Sorry, I feel pity to you. Go touch some grasses if you depressed.")

    @commands.command(name="slap", description="Menampar", aliases=["tampar"])
    async def slap(self, ctx:Context, *, member:discord.Member=None):
        if not member:
            return await ctx.send("Please write who you want to slap. ||Imagine slaping yourself. Are you even mad?||")

        api = requests.get("https://shiro.gg/api/images/slap").json()

        if ctx.author.id != member.id:
            embed = discord.Embed(
                title = f"{ctx.author.name} slap {member.name}",
                color = ctx.guild.me.color
            )
            embed.set_image(url=api["url"])
            await ctx.send(embed=embed)
        else:
            await ctx.reply("Sorry, I feel pity to you. Go touch grass if you depressed.")

async def setup(client):
    await client.add_cog(Interaction(client))
