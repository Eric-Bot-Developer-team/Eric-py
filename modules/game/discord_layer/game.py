import discord
from discord.ext import commands, tasks
from modules.game.logic_layer.connect4_logic import Connect4Logic, connect4games
from time import time


class Game(commands.Cog):

    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.easy_embed = self.bot.easy_embed
        self.timeout.start()

    @commands.command(name='conn')
    async def connect4(self, ctx, move=None):
        message = await Connect4Logic.connect4logic(ctx.author, ctx.channel, move)
        if message is not None:
            await self.easy_embed.simple_message(message, ctx)

    @tasks.loop(seconds=5.0)
    async def timeout(self):
        await self.bot.wait_until_ready()
        to_delete = []
        for key, value in connect4games.items():
            if time() - value.time > 120:
                to_delete.append(key)

        for key in to_delete:
            del connect4games[key]


def setup(bot):
    bot.add_cog(Game(bot))
