# This file handles any commands and sends them to the different modules.

# imports
import discord
from discord.ext import commands
import sys

def get_prefix(bot, message):
    prefixes = ['&', '#']

    if not message.guild:
        return '&'

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['modules.base.base']

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

# handle commands
if __name__ == '__main__':
    token = sys.argv[1]
    for extension in initial_extensions:
        bot.load_extension(extension)

    @bot.event
    async def on_ready():
        print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
        print(f'Successfully logged in and booted...!')


    bot.run(token, bot=True, reconnect=True)