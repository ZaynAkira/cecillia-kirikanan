import discord, platform, datetime, time, psutil
from discord.ext import commands
from discord.ext.commands.context import Context

class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command(aliases=['aboutbot', 'info', 'infobot', 'botinfo'])
    async def about(self, ctx:Context):
        embed = discord.Embed(
            title = "= Bot's Information =",
            color = ctx.guild.me.color
        )
        embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url_as(format="png", size=4096))

        embed.add_field(name="Name", value=f"[{self.client.user.name}](https://discord.gg/VhKVdmNsGq)")
        #
        member = discord.utils.find(lambda m: m.name == 'Kirikanan', ctx.guild.members)
        if member.status == discord.Status.online:
            if member.is_on_mobile():
                status = "<:mobilestatus:853831784114028584>"
            else:
                status = "<:green_circle:854258699908022302>"
        elif member.status == discord.Status.idle:
            status = "<:yellow_circle:854258886282313749>"
        elif member.status == discord.Status.dnd:
            status = "<:red_circle:854258993785733130>"
        elif member.status == discord.Status.offline or member.status == discord.Status.invisible:
            status = "<:white_circle:854259075608084480>"
        try:
            embed.add_field(name="Developer", value=f"{status} Kirikanan#4821")
        except:
            embed.add_field(name="Developer", value=f"Kirikanan#4821")
        embed.add_field(name="Date Created", value=self.client.user.created_at.strftime("%d/%m/%Y %H:%M:%S"))

        embed.add_field(name="Total Server", value=len(self.client.guilds))
        embed.add_field(name="Total User", value=len(self.client.users))
        #
        list_text_channel = []
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                list_text_channel.append(channel)
        embed.add_field(name="Total Channel", value=len(list_text_channel))
        list_text_channel.clear()

        embed.add_field(name="Library", value=f"discord.py v{discord.__version__}")
        embed.add_field(name="Program Language", value=f"Python v{platform.python_version()}")
        embed.add_field(name="Ping Bot", value=f"{round(self.client.latency*1000)}ms")

        embed.add_field(name="Online Time", value=str(datetime.timedelta(seconds=int(round(time.time()-startTime)))))
        embed.add_field(name="Total Emoji", value=len(self.client.emojis))
        embed.add_field(name="Bot ID", value=self.client.user.id)

        embed.add_field(name="Total Command", value=len(self.client.commands))
        embed.add_field(name="Operation System", value=platform.system())
        embed.add_field(name="Memory Usage", value=f"CPU: {psutil.cpu_percent()}%\nRAM: {psutil.virtual_memory().percent}%")

        embed.add_field(
            name="⠀",
            value="[Invite Cecillia!](https://discord.com/api/oauth2/authorize?client_id=864043720297938946&permissions=2044591350&scope=bot) | [Join Chrono Curses!](https://discord.gg/VhKVdmNsGq)",
            inline=False
        )

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(About(client))
