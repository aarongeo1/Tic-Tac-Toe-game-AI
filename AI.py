"""
Tic-Tac-Toe game created my Aaron Geo Binoy
Created using the minimax AI for recursive depth checking
file AI.py to be used with game.py for actual game implementation
Github: https://github.com/aarongeo1
Instagram: @aarongeo_
Discord: aarons#0143
"""
from cmath import inf
import copy


class computerplayer():
    def __init__(self, player, board):
        self.maxplayer = player
        self.board = board

    def win(self, board,turn):
        for row in [board[i*3:i*3+3]for i in range(3)]:
            if row.count(turn) == 3:
                return True
        for row in [board[i] + board[i+3] + board[i+6] for i in range(3)]:
            if row.count(turn) == 3:
                return True
        row = board[0]+board[4]+board[8]
        if row.count(turn) == 3:
            return True
        row = board[6]+board[4]+board[2]
        if row.count(turn) == 3:
            return True
        return False

    def available(self, board):
        empty = []
        for i in range(9):
            if board[i] == " ":
                empty += [i]
        return empty

    def Ai(self, turn):
        if self.available(self.board) != []:
            spot = self.available(self.board)[0]
        maxpoint = -inf
        for i in self.available(self.board):
            boards = copy.copy(self.board)
            point = self.minimax(boards, turn, i)
            if spot == i:
                maxpoint = point
            else:
                if point > maxpoint:
                    maxpoint, spot = point, i
        return spot

    
    def minimax(self, board,turn, spot):
        board[spot] = turn
        if self.win(board,turn) == True:
            if turn == self.maxplayer:
                x = 1
            else:
                x = -1
            point = (len(self.available(board)) + 1) * x
            # print(board)
            # print(point)
            return point
        if self.available(board) == []:
            return 0
        turn = "O" if turn == "X" else "X"
        if turn == self.maxplayer:
            maxpoint = -inf
            for i in self.available(board):
                newboard = copy.copy(board)
                point = self.minimax(newboard,turn,i)
                maxpoint = max(maxpoint,point)
            return maxpoint
        else:
            minpoint = inf
            for i in self.available(board):
                newboard = copy.copy(board)
                point = self.minimax(newboard,turn,i)
                minpoint = min(minpoint,point)
            return minpoint