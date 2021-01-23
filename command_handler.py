# This file handles any commands and sends them to the different modules.

# imports
import discord
import sys

# import bot modules
from modules.base.base import base
from modules.music.music import music

# handle commands
if __name__ == '__main__':

    token = sys.argv[1]
    prefix = "E"
    print("Token" + token)

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged on as {0}!'.format(client.user))

    @client.event
    async def on_message(message: discord.Message):
        if message.content[0] == prefix and message.author != client.user:
            args = message.content[2::].split(' ')
            module = args[0]
            module_args = args[1:]
            if(module == 'music'):
                await music(client, message, module_args)
            else:
                await base(client, message, args)


    client.run(token)
