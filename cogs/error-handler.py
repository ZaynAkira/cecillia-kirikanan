from discord.ext import commands

class ErrorHandle(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.EmojiNotFound):
            await ctx.reply("❌ **Emoji not found...**")
        elif isinstance(error, commands.RoleNotFound):
            await ctx.reply("❌ **Role not found...**")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply("❌ **Member not found...**")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.reply("❌ **Channel not found...**")

async def setup(client):
    await client.add_cog(ErrorHandle(client))
    
