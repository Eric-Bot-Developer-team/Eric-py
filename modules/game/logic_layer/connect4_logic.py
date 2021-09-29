from modules.game.games.connect4 import Game as connect4game
from discord.ext import tasks, commands

connect4games = {}


class Connect4Logic:

    @staticmethod
    async def connect4logic(author, channel, move=None):
        message = None
        draw = False

        if channel not in connect4games:
            connect4games[channel] = connect4game(author)
            message = f"Player 1 joined: {author}\n Waiting on Player 2 ..."
        else:
            game = connect4games[channel]
            game.reset_time()

            if game.player2.name is None and author != game.player1.name:
                game.player2.name = author
                message = f"\n{game.return_grid()}\n{game.player1.name}'s turn\n"

            if author in [game.player1.name, game.player2.name] and move == "stop":
                message = f"Game has been stopped."
                del connect4games[channel]

            if game.check_player(author) and move is not None:
                if len(move) == 1 and move.isdigit():
                    move = int(move) - 1
                    if author == game.player1.name and game.player1.turn == 1:
                        valid = game.change(move, game.player1.sign)
                        if valid:
                            draw = True
                            game.change_status()
                    elif author == game.player2.name and game.player2.turn == 1:
                        valid = game.change(move, game.player2.sign)
                        if valid:
                            draw = True
                            game.change_status()
                    has_won = game.check()
                    if draw and not has_won:
                        message = f"\n{game.return_grid()}\n{game.player1.name if game.player1.turn == 1 else game.player2.name}'s turn"
                    elif has_won:
                        message = f"\n{game.winner} has won!\n{game.return_grid()}\n"
                        del connect4games[channel]
        return message


def setup(bot):
    bot.add_cog(Connect4Logic(bot))
