# Eric
The Eric bot, a bot made by first year computer science students, that does basically everything.

##Local testing
Make a bot add [Discord developer portal](https://discord.com/developer)

Run command_handler with your bot token as first argument.

##Starting new module
Start a feature branch.  
Make modules/my_feature/my_feature.py  
Start with this code:  

    import discord
    from discord.ext import commands

    class my_feature(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
    
        @commands.command(name='my_command')
        async def cool_bot(self, ctx):
            await ctx.send('My command works')

    def setup(bot):
        bot.add_cog(my_feature(bot))

add my_feature to the following list in command_handler:

    initial_extensions = [..., 'my_feature']