import discord
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # for fun
    @commands.command(name='self-destruct')
    async def self_destruct(self, ctx):
        await ctx.send('beep boop bop **explodes**')

    # for testing if the bot is online
    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('Eric is alive.')

    # don't ask
    @commands.command(name='who-is-your-daddy')
    async def who_is_your_daddy(self, ctx):
        if ctx.author.id == 200721315471032322:
            await ctx.send('You are!')
        else:
            await ctx.send("WTF ew perv!")


def setup(bot):
    bot.add_cog(Base(bot))
