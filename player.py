
import numpy as np
import random
import pickle

from state import State

BOARD_COLS = 8
BOARD_ROWS = 8

class BotPlayer():
    
    def __init__(self):

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
    
    def getHash(self, board):
        return str(board.reshape(BOARD_COLS * BOARD_ROWS))

    def chooseAction(self, actions, board):

        # generate random number to determine if exploring or exploiting
        if random.random() <= self.explore:

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

    # two AI bots play against each other for trainig purposes
    def play(self, rounds=100):
       
        # number of episodes to train on
        num_eps = 100

        player_1 = self
        player_2 = BotPlayer()

        for _ in range(num_eps):

            # create a new game for each round
            # this reps the board
            state = State(player_1, player_2)

            # player_1 starts
            curr_player = player_1

            # run the game
            while not state.isEnd:

                # first look at all valid moves the curr player can make
                # note: getAvailablePositions() will return a dict where 
                # each key is curr_player's pieces (rep as a tup)
                # and each of those keys map to a list of tups that piece can move to
                positions = state.getAvailablePositions(curr_player)

                # then choose an action based on our Q-learning alg
                action = curr_player.chooseAction(positions, state)

                # then update state based on the chosen action
                state.updateState(action)

                # assign rewards
                # this is called after every update state
                # note: giveReward() calls feedReward()
                state.giveReward()

                # then add state to curr_player's states
                curr_player.addStates(curr_player.getHash())

                # swap turns
                curr_player = player_1 if curr_player == player_2 else player_2

            # reset game and run another episode
            player_1.reset()
            player_2.reset()

        # at very end of training we save policy
        self.savePolicy()

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
