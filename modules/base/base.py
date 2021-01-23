import discord
from discord.ext import commands

class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='self-destruct')
    async def self_destruct(self, ctx):
        await ctx.send('beep boop bop **explodes**')

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('Eric is alive.')

def setup(bot):
    bot.add_cog(base(bot))