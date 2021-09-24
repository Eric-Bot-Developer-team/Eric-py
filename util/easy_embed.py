import discord
import discord.ext.commands


async def simple_message(content, ctx: discord.ext.commands.Context, image_url=''):
    embed = discord.Embed(title=content, colour=0x7289da)
    if image_url:
        embed.set_image(url=image_url)
    await ctx.send(embed=embed)