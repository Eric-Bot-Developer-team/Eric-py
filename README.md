# Eric
The Eric bot, a bot made by first year computer science students, that does basically everything.

## Current modules

| Module        | Description           
| ------------- |-------------
| base          | The basics 
| music         | Simple youtube bot      

### Modules planned add:   

| Module        | Description           
| ------------- |-------------
| admin         | Administration 
| dank          | Memes and stuff 

## How to contribute

### Creating local setup 
clone    
-install ffmpeg (if testing music module)   
-install required packages
    
    python3 -m pip install -r requirements.txt
    
    
### Local testing
Make a bot at [Discord developer portal](https://discord.com/developer) and invite it to a test guild.

Run command_handler with your bot token as first argument.  
You can do this in Pycharm in configs in the right top corner:.

![pycharm](https://i.imgur.com/zGoLQ2D.png)

### Starting new module
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
(write your code in  class my_feature)
add my_feature to the following list in command_handler:

    initial_extensions = [..., 'my_feature']
    

