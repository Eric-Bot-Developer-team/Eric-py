import discord
from discord.ext import commands, tasks
from asyncio import sleep
from time import time
from easy_embed import simple_message
from modules.games.connect4 import Game as connect4game


connect4games = {}


class games(commands.Cog):

    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.timeout.start()

    @commands.command(name='conn')
    async def connect4(self, ctx, move=None):
        channel = ctx.channel
        author = ctx.author
        draw = False
        if channel not in connect4games and move is None:
            connect4games[channel] = connect4game(author)
            await simple_message(f"Player 1 joined: {author}\n Waiting on Player 2 ...", ctx)
        elif channel in connect4games:
            game = connect4games[channel]

            if game.player2.name is None and move is None and author != game.player1.name:
                game.player2.name = author
                game.reset_time()
                game.run = True
                await simple_message(f"Player 2 joined: {author}\n Game launching...", ctx)
                await sleep(1)
                await simple_message("\n" + game.return_grid() + f"\n{game.player1.name}'s turn\n", ctx)

            elif author == game.player1.name and game.player2.name is None and move is None:
                await simple_message("You can't join a game twice, you dummy lmao", ctx)

            elif author == game.player1.name and game.player2.name is None and move == "stop":
                await simple_message(f"Game has been stopped", ctx)
                del connect4games[channel]

            elif author == game.player1.name and game.player2.name is None and move is not None:
                await simple_message("Wait for an other person to join before trying moves out, you dummy lmao", ctx)

            if game.run:
                if game.check_player(author):
                    if move == 'stop':
                        del connect4games[channel]
                    elif move is not None:
                        if len(move) == 1 and move.isdigit():
                            move = int(move) - 1
                            if author == game.player1.name and game.player1.turn == 1:
                                valid = game.change(move, game.player1.sign)
                                if valid:
                                    draw = True
                                    game.change_status()
                                    game.reset_time()
                            elif author == game.player2.name and game.player2.turn == 1:
                                valid = game.change(move, game.player2.sign)
                                if valid:
                                    draw = True
                                    game.change_status()
                                    game.reset_time()
                            has_won = game.check()
                            if draw and not has_won:
                                await simple_message("\n" + game.return_grid() + f"\n{game.player1.name if game.player1.turn == 1 else game.player2.name}'s turn", ctx)
                            elif has_won:
                                await simple_message(f'\n{game.winner} has won!\n' + game.return_grid() + "\n", ctx)
                                del connect4games[channel]

    @tasks.loop(seconds=5.0)
    async def timeout(self):
        await self.bot.wait_until_ready()
        to_delete = []
        for key, value in connect4games.items():
            if time() - value.time > 120:
                to_delete.append(key)

        for key in to_delete:
            del connect4games[key]


def setup(bot):
    bot.add_cog(games(bot))