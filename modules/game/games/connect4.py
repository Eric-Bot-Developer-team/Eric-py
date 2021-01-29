from time import time


class Player:
    def __init__(self, sign, turn, name):
        self.name = name
        self.sign = sign
        self.turn = turn

class Game:
    def __init__(self, player):
        self.player1 = Player('🔵', 1, player)
        self.player2 = Player('🔴', 0, None)
        self.game = [["⚫" for _ in range(7)] for _ in range(6)]
        self.winner = None
        self.time = time()

    def return_grid(self):
        a = '1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n'
        for i in range(len(self.game)):
            a += f"{''.join(self.game[i])}\n"
        return a

    def change_status(self):
        self.player1.turn, self.player2.turn = self.player2.turn, self.player1.turn

    def change(self, num, sign):
        for i in range(5, -1, -1):
            if self.game[i][num] == "⚫":
                self.game[i][num] = sign
                return True
        return False

    def check(self):
        for i in range(6):
            for j in range(4):
                l = list(dict.fromkeys([self.game[i][j], self.game[i][j+1], self.game[i][j+2], self.game[i][j+3]]))
                if len(l) == 1 and l[0] != "⚫":
                    if l[0] == self.player1.sign:
                        self.winner = self.player1.name
                    else:
                        self.winner = self.player2.name
                    return True

        for j in range(7):
            for i in range(3):
                l = list(dict.fromkeys([self.game[i][j], self.game[i+1][j], self.game[i+2][j], self.game[i+3][j]]))
                if len(l) == 1 and l[0] != "⚫":
                    if l[0] == self.player1.sign:
                        self.winner = self.player1.name
                    else:
                        self.winner = self.player2.name
                    return True

        for i in range(0, -3, -1):
            for j in range(4):
                l = list(dict.fromkeys([self.game[2 + i][j], self.game[3 + i][1 + j], self.game[4 + i][2 + j], self.game[5 + i][3 + j]]))
                if len(l) == 1 and l[0] != "⚫":
                    if l[0] == self.player1.sign:
                        self.winner = self.player1.name
                    else:
                        self.winner = self.player2.name
                    return True

        for i in range(0, -3, -1):
            for j in range(0, -4, -1):
                l = list(dict.fromkeys([self.game[2 + i][6 + j], self.game[3 + i][5 + j], self.game[4 + i][4 + j], self.game[5 + i][3 + j]]))
                if len(l) == 1 and l[0] != "⚫":
                    if l[0] == self.player1.sign:
                        self.winner = self.player1.name
                    else:
                        self.winner = self.player2.name
                    return True
        return False

    def check_player(self, p):
        return (p == self.player1.name or p == self.player2.name) and (self.player2.name is not None)

    def reset_time(self):
        self.time = time()