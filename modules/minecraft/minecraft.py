# List of imports
# urlopen and json are imports that are used to read the api-value's
from urllib.request import urlopen
import json

# Standard import for discord command
from discord.ext import commands

# Ip-address of the server you want to track
ip = "axel.lorreyne.be"


# This method uses the api of mcsrvstat to get the information of the server and returns the total of online players
def get_online():
    respone = urlopen(f'https://api.mcsrvstat.us/2/{ip}')

    data = json.loads(respone.read())

    return int(data['players']['online'])


class Minecraft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="mc", invoke_without_command=False)
    async def minecraft(self, ctx):
        pass

    # Command
    @minecraft.command(name='online')
    async def online(self, ctx):
        # Get the current total of players that are online
        total_players = get_online()

        # Checking the value of total_players to make a correct response
        if total_players == 0:
            response_string = "are no players"
        elif total_players == 1:
            response_string = "is 1 player"
        else:
            response_string = f"are {total_players} players"

        # Send result
        await ctx.send(f"There {response_string} online on the minecraft server.")


def setup(bot):
    bot.add_cog(Minecraft(bot))
