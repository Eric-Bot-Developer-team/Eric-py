import discord
from discord.ext import commands

class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='self-destruct')
    async def cool_bot(self, ctx):
        await ctx.send('beep boop bop **explodes**')

def setup(bot):
    bot.add_cog(base(bot))