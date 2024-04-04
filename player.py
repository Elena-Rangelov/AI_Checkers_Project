
import numpy as np
import random

BOARD_COLS = 8
BOARD_ROWS = 8

class BotPlayer():
    def __init__(self):
        # christina
        # initiate function
    
    def getHash(self, board):
        return str(board.reshape(BOARD_COLS * BOARD_ROWS))

    def chooseAction(self, pos, board):

        if random.random() <= self.explore:
            p_id = random.choice(len(pos))
            action = pos[p_id]

        else:
            value_max = -999
            for p in pos:
                next = board.copy()
                next.updateState(p)
                next_hash = self.getHash(next)
                
                value = 0 if self.states_value.get(next_hash) is None else self.states_value.get(next_hash)

                if value >= value_max:
                    value_max = value
                    action = p

        return action

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