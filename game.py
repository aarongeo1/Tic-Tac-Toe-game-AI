"""
Tic-Tac-Toe game created my Aaron Geo Binoy
Created using the minimax AI for recursive depth checking
Github: https://github.com/aarongeo1
Instagram: @aarongeo_
Discord: aarons#0143
"""
from operator import truediv
import random
import copy
from AI import computerplayer

class tic_tac_toe():
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.winner = None
        self.human = random.choice(["X","O"])
        self.comp = "O" if self.human == "X" else "X"

    def start(self):
        board1 = [str(i) for i in range(9)]
        for row in [board1[j*3:j*3+3]for j in range(3)]:
            print("| "+" | ".join(row)+" |")
     
    def print_board(self):
        for row in [self.board[i*3:i*3+3]for i in range(3)]:
            print("| "+" | ".join(row)+" |")
        
    def make_move(self, player, mode):
        if mode == "AIvsAI":
            if self.human == player:
                boards = copy.copy(self.board)
                turn = player
                AI = computerplayer(turn, boards)
                spot = AI.Ai(turn)
                self.board[spot] = player
                print("AI has placed %s on %d"%(player,spot))
                return True
            elif self.comp == player:
                boards = copy.copy(self.board)
                turn = player
                AI = computerplayer(turn, boards)
                spot = AI.Ai(turn)
                self.board[spot] = player
                print("AI has placed %s on %d"%(player,spot))
                return True
        if mode == "AI":
            if self.human == player:
                spot = eval(input("move?: "))
                if self.board[spot] == " ":
                    self.board[spot] = player
                    return True
                else:
                    return False
            elif self.comp == player:
                boards = copy.copy(self.board)
                turn = player
                AI = computerplayer(turn, boards)
                spot = AI.Ai(turn)
                self.board[spot] = player
                print("AI has placed %s on %d"%(player,spot))
                return True

        if mode == "multi":
            spot = eval(input("move?: "))
            if self.board[spot] == " ":
                self.board[spot] = player
                return True
            else:
                return False
    
    def win(self, turn):
        for row in [self.board[i*3:i*3+3]for i in range(3)]:
            if row.count(turn) == 3:
                return True
        for row in [self.board[i] + self.board[i+3] + self.board[i+6] for i in range(3)]:
            if row.count(turn) == 3:
                return True
        row = self.board[0]+self.board[4]+self.board[8]
        if row.count(turn) == 3:
            return True
        row = self.board[6]+self.board[4]+self.board[2]
        if row.count(turn) == 3:
            return True
        return False

    def play(self):
        mode = "AIvsAI"
        self.start()
        turn = "X"
        self.make_move(turn, mode)
        self.print_board()
        while True:
            turn = "O" if turn == "X" else "X"
            if self.make_move(turn, mode) != True:
                print("invalid move")
                self.print_board()
                continue
            self.print_board()
            if self.win(turn) == True:
                print("%s wins!"%turn)
                break
            if self.count_empty() == 0:
                print("Its a tie!")
                break

    def count_empty(self):
        return self.board.count(" ")


       
if __name__ == '__main__':
    game = tic_tac_toe()
    game.play()
