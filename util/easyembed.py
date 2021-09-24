import discord
import discord.ext.commands


class EasyEmbed:

    def __init__(self, settings):
        self.color = discord.Color.from_rgb(*settings.values.color)

    async def simple_message(self, content, ctx: discord.ext.commands.Context, image_url=''):
        """Send an embed with an optional image"""
        embed = discord.Embed(title=content, colour=self.color)
        if image_url:
            embed.set_image(url=image_url)
        await ctx.send(embed=embed)
