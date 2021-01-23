import discord

async def music(client: discord.Client, message: discord.Message, args):
    if args[0] == 'test':
        await command_test(message)

async def command_test(message: discord.Message):
    await message.channel.send('Music is working!')