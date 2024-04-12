
import numpy as np
import random
import pickle

from state import State

BOARD_COLS = 8
BOARD_ROWS = 8

class Player():
    
    def __init__(self, first):

        # records all positions taken for training purposes
        self.states = []

        # how much Q-vals are updated towards newly calc Q-vals
        self.learning_rate = 0.2

        # we will be doing e-greedy
        # where 70% of the time, exploit: agent will take the greedy action (curr estimation of state-vals)
        # and the other 30%, explore: agent will take a random action
        self.exp_rate = 0.3

        # discount factor ( to do living reward)
        self.decay_gamma = 0.9

        # dict to update the corresponding state -> val
        self.states_value = {}

        self.first = first
    
    def getHash(self, board):
        return str(board.reshape(BOARD_COLS * BOARD_ROWS))

    def chooseAction(self, actions, board):

        # generate random number to determine if exploring or exploiting
        if random.random() <= self.exp_rate:

            #exploring - randomly choose an action from the list of actions
            pos = random.choice(len(actions))
            move = random.choice(len(actions[pos]))
            action = actions[pos][move]

        # exploiting
        else:
            value_max = -999
            for pos in actions: # nested loop
                for move in pos:
                    next = board.copy()
                    next.updateState(move)
                    next_hash = self.getHash(next)
                    
                    value = 0 if self.states_value.get(next_hash) is None else self.states_value.get(next_hash)
    
                    if value >= value_max:
                        value_max = value
                        result = move

        return result

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
<<<<<<< Updated upstream
        fr.close()

    ########### finish later
=======
        fr.close()
>>>>>>> Stashed changes
