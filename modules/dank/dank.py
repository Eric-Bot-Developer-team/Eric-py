import json
import random
from urllib.parse import quote_plus

import asyncpraw
import requests
from discord.ext import commands


class Dank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(client_id='vyMX9N2zNJds-GgIDktADg',
                             client_secret='R5IQUYXKssyWfvFrzG9jVuVfkTGMMA',
                             user_agent='windows:com.renevds.eric:1.0.0 (by u/renevds)')

    # for fun
    @commands.command(name='pp')
    async def pp(self, ctx):
        adjectives = json.loads(requests.get("https://random-word-form.herokuapp.com/random/adjective?count=3").text)

        await self.bot.easy_embed.simple_message(f'8{"=" * random.randrange(10)}D', ctx,
                                                 description=f'You have a {", ".join(adjectives)} cock!\n')

    @commands.command(name='doge')
    async def doge(self, ctx, *args):
        API = "https://api.funtranslations.com/translate/doge.json?text="

        doge = json.loads(requests.get(API + quote_plus(' '.join(args))).text)['contents']['translated']
        await ctx.message.delete()
        await ctx.send(f'**{ctx.message.author.name}**: {doge}')

    @commands.command()
    async def meme(self, ctx):
        subreddit = await self.reddit.subreddit('memes')

        all_subs = ['memes']

        top = subreddit.top(limit=100)  # bot will choose between the top 250 memes

        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        url = random_sub.url

        while not '.jpg' in url or '.png' in url:
            random_sub = random.choice(all_subs)
            url = random_sub.url

        await ctx.send(url)


def setup(bot):
    bot.add_cog(Dank(bot))
