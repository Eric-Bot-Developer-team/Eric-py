# List of imports
# urlopen and json are imports that are used to read the api-value's
import json

# Standard import for discord command
import requests
from discord.ext import commands

# Ip-address of the server you want to track
ip = "informaticautisme.com"


# This method uses the api of mcsrvstat to get the information of the server and returns this info in a json object
def get_server_data():
    #this should be fixed to verify=True
    response = requests.get(f'https://api.mcsrvstat.us/2/{ip}', verify=False)
    return json.loads(response.text)


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
        total_players = int(get_server_data()['players']['online'])

        # Checking the value of total_players to make a correct response
        if total_players == 0:
            response_string = "are no players"
        elif total_players == 1:
            response_string = "is 1 player"
        else:
            response_string = f"are {total_players} players"

        # Send result
        await ctx.send(f"There {response_string} online on the minecraft server.")

    # Command to see who is online
    @minecraft.command(name='who')
    async def who(self, ctx):
        # Get list of players who are online
        data = get_server_data()
        list_of_players = data['players']['list']
        # get servername
        servername = data['hostname']
        # Returned embed message with servername and player(s) on different lines
        await self.easy_embed.simple_message(f'Player(s) online on "{servername}"\n\n', ctx,
                                             description="\n".join(sorted(list_of_players)))


def setup(bot):
    bot.add_cog(Minecraft(bot))
