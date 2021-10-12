# List of imports
# urlopen and json are imports that are used to read the api-value's
import json

# Standard import for discord command
import requests
from discord.ext import commands

# Ip-address of the server you want to track
from mcstatus import MinecraftServer

ip = "informaticautisme.com"
port = 25565

server = MinecraftServer(ip, port)


class Minecraft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.easy_embed = self.bot.easy_embed

    @commands.group(name="mc", invoke_without_command=False)
    async def minecraft(self, ctx):
        pass

    # Command to check how many players are online
    @minecraft.command(name='online')
    async def online(self, ctx):
        # Get the current total of players that are online
        total_players = server.status().players.online

        # Checking the value of total_players to make a correct response
        if total_players == 0:
            response_string = "are no players"
        elif total_players == 1:
            response_string = "is 1 player"
        else:
            response_string = f"are {total_players} players"

        # Send result
        await self.easy_embed.simple_message(f"There {response_string} online on the minecraft server.", ctx)

    # Command to see who is online
    @minecraft.command(name='who')
    async def who(self, ctx):
        # Get list of players who are online
        list_of_players = [i['name'] for i in server.status().raw['players']['sample']]

        # Returned embed message with servername and player(s) on different lines
        await self.easy_embed.simple_message(f'Player(s) online on "{ip}"\n\n', ctx,
                                             description="\n".join(sorted(list_of_players)))


def setup(bot):
    bot.add_cog(Minecraft(bot))
