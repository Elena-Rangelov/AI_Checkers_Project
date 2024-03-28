
import numpy as np

BOARD_COLS = 8
BOARD_ROWS = 8

class BotPlayer():
    def __init__(self):
        # christina
        # initiate function
    
    def getHash(self, board):
        return str(board.reshape(BOARD_COLS * BOARD_ROWS))

    def chooseAction(self, pos, board):
        # el
        # choose action

    def addStates(self, board_hash):
        self.states.append(board_hash)

    def feedReward(self, reward):
        # wren
        # assign rewards

    def play(self, rounds=100):
        # christina
        # play

    def reset(self):
        self.states = []

    def savePolicy(self):
        # wren
        # save policy

    def loadPolicy(self):
        # wren
        # load policy

    ########### finish later