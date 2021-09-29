![](https://github.com/Eric-Bot-Developer-team/Eric-py/blob/main/logo.png?raw=true)

# Eric
The Eric bot, a bot made by first year computer science students, that does basically everything.

## Current modules

| Module        | Description           
| ------------- |-------------
| base          | The basics 
| music         | Simple youtube bot
| dank          | Memes and stuff 
| game          | Games

### Modules planned add:   

| Module        | Description           
| ------------- |-------------
| admin         | Administration

## How to contribute

### Creating local setup  
-install ffmpeg (if using music module)   
-install required packages with:
    
    python3 -m pip install -r requirements.txt
    
    
### Local testing
Make a bot at [Discord developer portal](https://discord.com/developer) and invite it to a test guild.
- Creat an environment variable `TOKEN=your_bot_token`
- Run command_handler

### Starting new module
Start a feature branch.  
Make modules/my_module/my_module.py  
Start with this code:  

    import discord
    from discord.ext import commands

    class my_feature(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
    
        @commands.command(name='my_module')
        async def cool_bot(self, ctx):
            await ctx.send('My command works')

    def setup(bot):
        bot.add_cog(my_feature(bot))
(write your code in  class my_feature)
add my_feature to the following list in command_handler:

    initial_extensions = [..., 'my_feature']
    

