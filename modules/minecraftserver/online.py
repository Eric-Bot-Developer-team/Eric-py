from urllib.request import urlopen
import json
import discord
from discord.ext import commands

ip = "axel.lorreyne.be"


class Online(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='online')
    async def cool_bot(self, ctx):
        temp = self.get_online()
        if temp == 0:
            responsestring = "There are no players online on the minecraft server"
        elif temp == 1:
            responsestring = "There is 1 player online on the minecraft server"
        else:
            responsestring = f"There are {temp} players online on the minecraft server"
        await ctx.send(responsestring)

    def get_online(self):
        respone = urlopen(f'https://api.mcsrvstat.us/2/{ip}')

        data = json.loads(respone.read())

        return int(data["players"]["online"])


def setup(bot):
    bot.add_cog(Online(bot))
