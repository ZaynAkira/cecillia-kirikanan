import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member

class Moderasi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="ban", description="Meng-Ban seseorang.")
    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def ban(self, ctx:Context, member:Member=None, *, alasan:str=None):
        if not member:
            return await ctx.send("Tuliskan orang yang mau kamu ban serta alasannya!\nContoh: `c.ban @Kirikanan#4821 nakal`")

        alasan = "Tidak ada." if not alasan else alasan

        await member.ban()

        embed = discord.Embed(
            description = f"**Alasan:** {alasan}",
            color = member.color
        )
        embed.set_author(name=f"{member} di-Ban", icon_url=member.avatar_url)
        await ctx.send(embed=embed)

        if alasan is None:
            await member.send(f"Maaf, kamu telah di-ban dari server **{ctx.guild.name}**.")
        else:
            await member.send(f"Maaf, kamu telah di-ban dari server **{ctx.guild.name}** dengan alasan **{alasan}**.")
    @ban.error
    async def on_ban_error(self, ctx:Context, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Kamu tidak punya izin untuk menjalankan perintah ini!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("Saya tidak memiliki izin `Ban Members`!")

    @commands.command(name="kick", description="Mengeluarkan seseorang.")
    @commands.has_guild_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    async def kick(self, ctx:Context, member:Member=None, *, alasan:str=None):
        if not member:
            return await ctx.send("Tuliskan member yang ingin kamu kick.\nContoh: `c.kick @Kirikanan#4821 absurd`")

        alasan = "Tidak ada." if not alasan else alasan

        await member.kick(reason=alasan)

        embed = discord.Embed(
            description = f"**Alasan:** {alasan}",
            color = member.color
        )
        embed.set_author(name=f"{member} Dikeluarkan", icon_url=member.avatar_url)
        await ctx.send(embed=embed)

        if alasan is None:
            await member.send(f"Maaf, kamu telah dikeluarkan dari server **{ctx.guild.name}**.")
        else:
            await member.send(f"Maaf, kamu telah dikeluarkan dari server **{ctx.guild.name}** dengan alasan **{alasan}**.")
    @kick.error
    async def on_kick_error(self, ctx:Context, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Kamu tidak punya izin untuk menjalankan perintah ini!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("Saya tidak memiliki izin `Kick Members`!")

    @commands.command(name="add-role", aliases=["add-roles", "addrole", "addroles"], description="Memberikan Role kepada seseorang.")
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def addrole(self, ctx:Context, member:discord.Member=None, role:discord.Role=None):
        if not member:
            return await ctx.send("Tuliskan member yang mau kamu berikan role, dan role-nya yang mau kamu berikan.\nContoh: `c.add-role @Kirikanan#4821 @AI Bot`")
        elif not role and member != None:
            return await ctx.send(f"Tuliskan Role yang mau kamu berikan.\nContoh: `c.add-role @{member} @Manusia`")

        await member.add_roles(role)

        embed = discord.Embed(
            description = f"Role {role.mention} diberikan kepada {member.mention}.",
            color = role.color
        )
        embed.set_author(name="Role Diberikan", icon_url=member.avatar_url)
        await ctx.send(embed=embed)
    @addrole.error
    async def on_addrole_error(self, ctx:Context, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Kamu tidak punya izin untuk menjalankan perintah ini!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("Saya tidak memiliki izin `Manage Roles`!")

    @commands.command(name="remove-role", aliases=["remove-roles", "removerole", "removeroles"], description="Memberikan Role kepada seseorang.")
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def removerole(self, ctx:Context, member:discord.Member=None, role:discord.Role=None):
        if not member:
            return await ctx.send("Tuliskan member yang mau kamu cabut role-nya, dan role-nya yang mau kamu cabut.\nContoh: `c.remove-role @Kirikanan#4821 @AI Bot`")
        elif not role and member != None:
            return await ctx.send(f"Tuliskan Role yang mau kamu cabut.\nContoh: `c.remove-role @{member} @Manusia`")

        await member.remove_roles(role)

        embed = discord.Embed(
            description = f"Role {role.mention} dicabut dari {member.mention}.",
            color = role.color
        )
        embed.set_author(name="Role Dicabut", icon_url=member.avatar_url)
        await ctx.send(embed=embed)
    @removerole.error
    async def on_removerole_error(self, ctx:Context, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Kamu tidak punya izin untuk menjalankan perintah ini!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("Saya tidak memiliki izin `Manage Roles`!")

    @commands.command(name="purge", aliases=["clear"], description="Menghapus pesan.")
    async def purge(self, ctx:Context, jumlah:int=None):
        if not jumlah:
            return await ctx.send("Masukkan jumlah pesan yang ingin kamu hapus.\nContoh: `c.purge 3`")

        await ctx.channel.purge(limit=jumlah+1)
        await ctx.send(f"Berhasil menghapus {jumlah} pesan.", delete_after=2.5)
    @purge.error
    async def on_purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Kamu tidak punya izin untuk menjalankan perintah ini!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("Saya tidak memiliki izin `Manage Messages`!")

    @commands.group(name="slowmode", description="Mengatur mode lambat.", invoke_without_command=True)
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def slowmode(self, ctx:Context, durasi:int=None):
        if not durasi:
            return await ctx.send("Tuliskan durasi waktu untuk mode lambatnya *dalam bentuk detik*.\nContoh: `c.slowmode 5`")

        await ctx.channel.edit(slowmode_delay=durasi)

        embed = discord.Embed(
            title = "Slowmode Diterapkan",
            description = f"Channel ini sekarang dipakaikan slowmode dengan durasi {durasi} detik.",
            color = ctx.guild.me.color
        )
        embed.set_footer(text="Tip: untuk mematikannya, cukup ketik 'c.slowmode off'")
        await ctx.send(embed=embed)
    @slowmode.command()
    async def off(self, ctx:Context):
        await ctx.channel.edit(slowmode_delay=0)
        embed = discord.Embed(
            title = "Slowmode Dimatikan",
            description = f"Channel ini sekarang dimatikan slowmode-nya.",
            color = ctx.guild.me.color
        )
        await ctx.send(embed=embed)
    @slowmode.error
    async def on_slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Kamu tidak punya izin untuk menjalankan perintah ini!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("Saya tidak memiliki izin `Manage Channels`!")


def setup(client): client.add_cog(Moderasi(client))
