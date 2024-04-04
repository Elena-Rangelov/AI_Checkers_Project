
import numpy as np
import random
import pickle

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
        # Loop through the states the player went through
        for curr in reversed(self.states):
            # Initializes state value if not encountered before
            if self.states_value.get(curr) is None:
                self.states_value[curr] = 0
            # Use value iteration formula
            self.states_value[curr] += self.lr * (self.decay_gamma * reward - self.states_value[curr])
            # Updates reward for next iteration
            reward = self.states_value[curr]

    def play(self, rounds=100):
        # christina
        # play

    def reset(self):
        self.states = []

    # Using pickle module to save and load policies
    def savePolicy(self):
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()

    ########### finish later