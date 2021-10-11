import discord
import discord.ext.commands


class EasyEmbed:

    def __init__(self, bot: discord.Client):
        self.color = discord.Color.from_rgb(*bot.settings.values.style.color)
        self.bot = bot

    async def simple_message(self, content, channel, image_url='', description=''):
        """Send an embed with an optional imagen, takes a ctx or a channel id as channel parameter."""

        if not isinstance(channel, discord.ext.commands.Context):
            channel = self.bot.get_channel(int(channel))

        embed = discord.Embed(title=content, description=description, colour=self.color)
        if image_url:
            embed.set_image(url=image_url)
        await channel.send(embed=embed)
