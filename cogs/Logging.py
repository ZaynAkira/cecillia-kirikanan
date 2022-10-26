import discord
from discord.ext import commands
from discord.guild import Guild
from discord.invite import Invite
from discord.member import Member, VoiceState
from discord.role import Role
from discord.user import User

aoa = {
    834965728658456606: 862296825478381598, #i my me
    791704671915081768: 862869693982834688, #chrono curses
}

EXCEPTED_CHANNEL_ID = 791713394700189706

class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):
        embed = discord.Embed(
            title = "Pesan Dihapus",
            description = f"Pesan yang dikirim oleh {message.author.mention} pada channel {message.channel.mention} dihapus.",
            color = 0xff0000
        )
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)

        embed.add_field(name="Isi Pesan", value=message.content)

        embed.set_footer(text=f"ID Pesan: {message.id} | ID Pengirim: {message.author.id}")

        if int(message.guild.id) in aoa.keys():
            if message.channel != discord.utils.get(self.client.get_all_channels(), id=EXCEPTED_CHANNEL_ID):
                await self.client.get_channel(aoa[message.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before:discord.Message, after:discord.Message):
        embed = discord.Embed(
            title = "Pesan Diedit",
            description = f"Pesan diedit pada channel {before.channel.mention}",
            color = before.author.color
        )
        embed.set_author(name=before.author, icon_url=before.author.avatar_url)

        embed.add_field(name="Sebelum", value=before.content)
        embed.add_field(name="Setelah", value=after.content)

        embed.set_footer(text=f"ID Pesan: {after.id} | ID Pengirim: {before.author.id}")

        if int(before.guild.id) in aoa.keys():
            if before.channel != discord.utils.get(self.client.get_all_channels(), id=EXCEPTED_CHANNEL_ID):
                await self.client.get_channel(aoa[before.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel:discord.abc.GuildChannel):
        embed = discord.Embed(
            title = "Channel Dibuat",
            description = f"Channel {channel.mention} (`{channel.name}`) dibuat.",
            color = 0x00ff00 #hijau
        )
        embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
        embed.set_footer(text=f"ID Server: {channel.guild.id}")
        
        if int(channel.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[channel.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel:discord.abc.GuildChannel):
        embed = discord.Embed(
            title = "Channel Dihapus",
            description = f"Channel **#{channel.name}** dihapus.",
            color = 0xff0000 #merah
        )
        embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
        embed.set_footer(text=f"ID Server: {channel.guild.id}")
        
        if int(channel.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[channel.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before:discord.abc.GuildChannel, after:discord.abc.GuildChannel):
        if before.name != after.name:
            embed = discord.Embed(
                title = "Channel Berganti Nama",
                description = f"Channel **#{before.name}** berubah nama menjadi **#{after.name}**",
                color = 0x00ff00 #hijau
            )
            embed.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
            embed.set_footer(text=f"ID Server: {after.guild.id}")
            if int(after.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[after.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        embed = discord.Embed(
            title = "Seseorang Bergabung",
            description = f"{member.mention} bergabung, sekarang server sudah memiliki {len(member.guild.members)} member.",
            color = 0x00ff00
        )
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_footer(text=f"ID: {member.id} | ID Server: {member.guild.id}")
        embed.set_thumbnail(url=member.avatar_url_as(format=None, static_format="png", size=4096))
        if int(member.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[member.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member:discord.Member):
        embed = discord.Embed(
            title = "Seseorang Keluar",
            description = f"{member.mention} keluar dari server :'v, sekarang server tinggal memiliki {len(member.guild.members)} member.",
            color = 0xff0000
        )
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_footer(text=f"ID: {member.id} | ID Server: {member.guild.id}")
        embed.set_thumbnail(url=member.avatar_url_as(format=None, static_format="png", size=4096))
        if int(member.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[member.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_update(self, before:discord.Guild, after:discord.Guild):
        if before.name != after.name:
            embed = discord.Embed(
                title = "Server Berganti Nama",
                description = f"Server {after.name} berganti nama.",
                color = 0x00ff00
            )
            embed.set_author(name=after.name, icon_url=after.name)

            embed.add_field(name="Sebelum", value=before.name)
            embed.add_field(name="Sesudah", value=after.name)

            embed.set_footer(text=f"ID Server: {after.id}")
            if int(after.id) in aoa.keys():
                await self.client.get_channel(aoa[after.id]).send(embed=embed)
        elif before.icon_url != after.icon_url:
            embed = discord.Embed(
                title = "Foto Server Berubah",
                description = f"Foto server {after.name} berubah menjadi:",
                color = 0x00ff00
            )
            embed.set_author(name=after.name, icon_url=after.icon_url)

            embed.set_thumbnail(url=before.icon_url)
            embed.set_image(url=after.icon_url)

            embed.set_footer(text=f"ID Server: {after.id}")
            if int(after.id) in aoa.keys():
                await self.client.get_channel(aoa[after.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role:discord.Role):
        embed = discord.Embed(
            title = "Role Dibuat",
            description = f"Ada Role yang baru saja dibuat, yaitu {role.mention} (`{role.name}`).",
            color = 0x00ff00
        )
        embed.set_author(name=role.guild.name, icon_url=role.guild.icon_url)
        embed.set_footer(text=f"ID Role: {role.id} | ID Server: {role.guild.id}")
        if int(role.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[role.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before:Role, after:Role):
        def bikin_embed(title:str, desc:str, sebelum, sesudah, warna=None):
            warna = after.color if not warna else warna

            embed = discord.Embed(
                title = title,
                description = desc,
                color = warna
            )
            embed.set_author(name=before.guild.name, icon_url=before.guild.icon_url)

            embed.add_field(name="Sebelum", value=sebelum)
            embed.add_field(name="Setelah", value=sesudah)

            embed.set_footer(text=f"ID Role: {before.id} | ID Server: {before.guild.id}")

            return embed

        if before.name != after.name:
            if int(before.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[before.guild.id]).send(embed=bikin_embed(
                    title = "Role Berganti Nama",
                    desc = f"Role {after.mention} berubah nama.",
                    sebelum = before.name,
                    sesudah = after.name
                ))
        elif before.position != after.position:
            if int(before.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[before.guild.id]).send(embed=bikin_embed(
                    title = "Role Berganti Posisi",
                    desc = f"Role {after.mention} berubah posisi.",
                    sebelum = before.position,
                    sesudah = after.position
                ))
        elif before.color != after.color:
            if int(before.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[before.guild.id]).send(embed=bikin_embed(
                    title = "Role Berganti Warna",
                    desc = f"Role {after.mention} berubah warna.",
                    sebelum = str(before.color).upper(),
                    sesudah = str(after.color).upper()
                ))

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role:discord.Role):
        embed = discord.Embed(
            title = "Role Dihapus",
            description = f"Ada Role yang baru saja dihapus, yaitu **@{role.name}**.",
            color = 0xff0000
        )
        embed.set_author(name=role.guild.name, icon_url=role.guild.icon_url)
        embed.set_footer(text=f"ID Role: {role.id} | ID Server: {role.guild.id}")
        if int(role.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[role.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member:Member, before:VoiceState, after:VoiceState):
        if before.channel == None:
            embed = discord.Embed(
                title = "Seseorang Memasuki Voice Channel",
                description = f"{member.mention} memasuki voice channel **{after.channel}**.",
                color = 0x00ff00 #hijau
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.set_footer(text=f"ID User: {member.id}")
            embed.set_thumbnail(url=member.avatar_url_as(format=None, static_format="png", size=4096))
            if int(member.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[member.guild.id]).send(embed=embed)
        elif after.channel == None:
            embed = discord.Embed(
                title = "Seseorang Keluar dari Voice Channel",
                description = f"{member.mention} keluar dari voice channel **{before.channel}**.",
                color = 0xff0000 #merah
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.set_footer(text=f"ID User: {member.id}")
            embed.set_thumbnail(url=member.avatar_url_as(format=None, static_format="png", size=4096))
            if int(member.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[member.guild.id]).send(embed=embed)
        elif before.channel != after.channel:
            embed = discord.Embed(
                title = "Seseorang Berpindah Voice Channel",
                description = f"{member.mention} berpindah voice channel.",
                color = member.color
            )
            embed.add_field(name="Dari", value=f"**{before.channel}**")
            embed.add_field(name="Ke", value=f"**{after.channel}**")

            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.set_footer(text=f"ID User: {member.id}")
            embed.set_thumbnail(url=member.avatar_url_as(format=None, static_format="png", size=4096))
            if int(member.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[member.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before:Member, after:Member):
        if before.display_name != after.display_name:
            embed = discord.Embed(
                title = "Seseorang Berganti Nickname",
                description = f"{after.mention} berubah nama.",
                color = before.color
            )
            embed.add_field(name="Sebelum", value=before.display_name)
            embed.add_field(name="Setelah", value=after.display_name)

            embed.set_author(name=before, icon_url=before.avatar_url)
            embed.set_thumbnail(url=before.avatar_url_as(format=None, static_format="png", size=4096))
            embed.set_footer(text=f"ID User: {before.id}")
            if int(before.guild.id) in aoa.keys():
                await self.client.get_channel(aoa[before.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_invite_create(self, invite:Invite):
        embed = discord.Embed(
            title = "Link Invite Dibuat",
            description = f"{invite.inviter.mention} membuat link invite.\n{invite.url}",
            color = 0x00ff00
        )
        embed.set_author(name=invite.guild, icon_url=invite.guild.icon_url)
        embed.set_footer(text=f"ID Server: {invite.guild.id} | ID Link Invite: {invite.id}")
        if int(invite.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[invite.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_invite_delete(self, invite:Invite):
        embed = discord.Embed(
            title = "Link Invite Dihapus",
            description = f"{invite.inviter.mention} menghapus link invite.\n`{invite.url}`",
            color = 0xff0000
        )
        embed.set_author(name=invite.guild, icon_url=invite.guild.icon_url)
        embed.set_footer(text=f"ID Server: {invite.guild.id} | ID Link Invite: {invite.id}")
        if int(invite.guild.id) in aoa.keys():
            await self.client.get_channel(aoa[invite.guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild:Guild, user):
        embed = discord.Embed(
            title = "Seseorang di-Ban",
            description = f"{user.mention} kena Ban.",
            color = 0xff0000
        )
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url_as(format=None, static_format="png", size=4096))
        embed.set_footer(text=f"ID User: {user.id} | ID Server: {guild.id}")
        if int(guild.id) in aoa.keys():
            await self.client.get_channel(aoa[guild.id]).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild:Guild, user:User):
        embed = discord.Embed(
            title = "Seseorang di-Unban",
            description = f"{user.mention} dibebaskan dari Ban.",
            color = 0x00ff00
        )
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url_as(format=None, static_format="png", size=4096))
        embed.set_footer(text=f"ID User: {user.id} | ID Server: {guild.id}")
        if int(guild.id) in aoa.keys():
            await self.client.get_channel(aoa[guild.id]).send(embed=embed)

async def setup(client):
    await client.add_cog(Log(client))
