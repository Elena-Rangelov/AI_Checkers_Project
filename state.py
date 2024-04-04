import numpy as np

BOARD_COLS = 8
BOARD_ROWS = 8

class State():
    def __init__(self, p1, p2):
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 2, 0, 2, 0, 2, 0],
                    [0, 2, 0, 2, 0, 2, 0, 2],
                    [2, 0, 2, 0, 2, 0, 2, 0]]

        self.p1 = p1
        self.p2 = p2

        self.isEnd = False
        self.boardHash = None

    def getHash(self):
        self.boardHash = str(self.board.reshape(BOARD_COLS * BOARD_ROWS))
        return self.boardHash

    def getAvailablePositions(self, p):
        positions = {}
        for i in range(self.BOARD_COLS):
            for j in range(self.BOARD_ROWS):
                if p.first:
                    if self.board[i][j]%2 == 1:

                        if self.board[i-1][j-1] == 0:
                            positions[(i, j)] += [(i-1, j-1)]
                        elif self.board[i-1][j-1] != 0 and self.board[i-1][j-1]%2 == 0 and self.board[i-2][j-2]:
                            positions[(i, j)] += [(i-2, j-2)]

                        if self.board[i+1][j-1] == 0:
                            positions[(i, j)] += [(i+1, j-1)]
                        elif self.board[i+1][j-1] != 0 and self.board[i+1][j-1]%2 == 0 and self.board[i+2][j-2]:
                            positions[(i, j)] += [(i+2, j-2)]

                        if self.board[i][j] == 3:

                            if self.board[i+1][j+1] == 0:
                                positions[(i, j)] += [(i+1, j+1)]
                            elif self.board[i+1][j+1] != 0 and self.board[i+1][j+1]%2 == 0 and self.board[i+2][j+2]:
                                positions[(i, j)] += [(i+2, j+2)]

                            if self.board[i-1][j+1] == 0:
                                positions[(i, j)] += [(i-1, j+1)]
                            elif self.board[i-1][j+1] != 0 and self.board[i-1][j+1]%2 == 0 and self.board[i-2][j+2]:
                                positions[(i, j)] += [(i-2, j+2)]
                        
                else:
                    if self.board[i][j]%2 == 0 and self.board[i][j] != 0:

                        if self.board[i+1][j+1] == 0:
                            positions[(i, j)] += [(i+1, j+1)]
                        elif self.board[i+1][j+1]%2 == 1 and self.board[i+2][j+2]:
                            positions[(i, j)] += [(i+2, j+2)]

                        if self.board[i-1][j+1] == 0:
                            positions[(i, j)] += [(i-1, j+1)]
                        elif self.board[i-1][j+1] != 0 and self.board[i-1][j+1]%2 == 0 and self.board[i-2][j+2]:
                            positions[(i, j)] += [(i-2, j+2)]

                        if self.board[i][j] == 3:

                            if self.board[i-1][j-1] == 0:
                                positions[(i, j)] += [(i-1, j-1)]
                            elif self.board[i-1][j-1] != 0 and self.board[i-1][j-1]%2 == 0 and self.board[i-2][j-2]:
                                positions[(i, j)] += [(i-2, j-2)]

                            if self.board[i+1][j-1] == 0:
                                positions[(i, j)] += [(i+1, j-1)]
                            elif self.board[i+1][j-1] != 0 and self.board[i+1][j-1]%2 == 0 and self.board[i+2][j-2]:
                                positions[(i, j)] += [(i+2, j-2)]
                        

    def winner(self):
        # checking end state
        # christina

    def updateState(self, pos):
        # kaan
        # update the board

    def reset(self):
        # kaan
        # reset board

    def giveReward(self):
        # kaan
        # assign rewards

    ############################# FOR LATER
    def playHuman(self):
        # play human

    def showBoard(self):
        # gui display
    



