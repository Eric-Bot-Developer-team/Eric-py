# This file handles any commands and sends them to the different modules.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from util.easyembed import EasyEmbed
from util.settings_builder import Settings


def get_prefix(bot, message):
    prefixes = ['&', '#', 'E ', '& ', 'E']

    if not message.guild:
        return '&'

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['modules.base.base', 'modules.music.music', 'modules.dank.dank',
                      'modules.game.discord_layer.game',
                      'modules.minecraft.minecraft']

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

# handle commands
if __name__ == '__main__':

    bot.settings = Settings()

    bot.easy_embed = EasyEmbed(bot)

    for extension in initial_extensions:
        bot.load_extension(extension)


    @bot.event
    async def on_ready():
        print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
        print(f'Successfully logged in and booted...!')

    load_dotenv()
    bot.run(os.environ['TOKEN'], bot=True, reconnect=True)
