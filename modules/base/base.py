import discord

async def base(client: discord.Client, message: discord.Message, args):
    subcommand = args[0]

    if subcommand == 'test':
        await send_text(message, 'Eric is alive!')
    elif subcommand == 'self-destruct':
        await send_text(message, 'Beep bop boop **explodes**')


async def send_text(message: discord.Message, text):
    await message.channel.send(text)