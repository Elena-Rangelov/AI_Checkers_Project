import numpy as np

BOARD_COLS = 8
BOARD_ROWS = 8

class State():
    def __init__(self, p1, p2):
        self.board = np.array([[0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 2, 0, 2, 0, 2, 0],
                    [0, 2, 0, 2, 0, 2, 0, 2],
                    [2, 0, 2, 0, 2, 0, 2, 0]])

        self.p1 = p1
        self.p2 = p2

        self.isEnd = False
        self.boardHash = None

    def getHash(self):
        self.boardHash = str(self.board.reshape(BOARD_COLS * BOARD_ROWS))
        return self.boardHash

    def getAvailablePositions(self, p):
        positions = {}
        for i in range(BOARD_COLS):
            for j in range(BOARD_ROWS):

                positions[(i, j)] = []


                # if first player, use 1 and 3
                if p.first:

                    # if the current spot is our piece
                    if self.board[i][j]%2 == 1:

                        # add first diagonal and possible jump
                        if i-1 >= 0 and j-1 >= 0:
                            if self.board[i-1][j-1] == 0:
                                positions[(i, j)].append([(i, j), (i-1, j-1)])
                            elif i-2 >= 0 and j-2 >= 0 and self.board[i-1][j-1] != 0 and self.board[i-1][j-1]%2 == 0 and self.board[i-2][j-2] == 0:
                                positions[(i, j)].append([(i, j), (i-1, j-1), (i-2, j-2)])

                            # failed attempt at incoporating multiple jumps - for later
                                
                            # b = True
                            # while b:
                            #     if self.board[i-1][j-1] != 0 and self.board[i-1][j-1]%2 == 0 and self.board[i-2][j-2]:
                            #     positions[(i, j)] += [(i-2, j-2)]
                            #     if

                        # add second diagonal and possible jump
                        if i+1 < BOARD_COLS and j-1 >= 0:
                            if self.board[i+1][j-1] == 0:
                                positions[(i, j)].append([(i, j), (i+1, j-1)])
                            elif i+2 < BOARD_COLS and j-2 >= 0 and self.board[i+1][j-1] != 0 and self.board[i+1][j-1]%2 == 0 and self.board[i+2][j-2] == 0:
                                positions[(i, j)].append([(i, j), (i+1, j-1), (i+2, j-2)])

                        # if the piece is our queen piece
                        if self.board[i][j] == 3:

                            # add on the other two diagonals and possible jumps
                            if i+1 < BOARD_COLS and j+1 < BOARD_COLS:
                                if self.board[i+1][j+1] == 0:
                                    positions[(i, j)].append([(i, j), (i+1, j+1)])
                                elif i+2 < BOARD_COLS and j+2 < BOARD_COLS and self.board[i+1][j+1] != 0 and self.board[i+1][j+1]%2 == 0 and self.board[i+2][j+2] == 0:
                                    positions[(i, j)].append([(i, j), (i+1, j+1), (i+2, j+2)])

                            if i-1 >= 0 and j+1 < BOARD_COLS:
                                if self.board[i-1][j+1] == 0:
                                    positions[(i, j)].append([(i, j), (i-1, j+1)])
                                elif i-2 >= 0 and j+2 < BOARD_COLS and self.board[i-1][j+1] != 0 and self.board[i-1][j+1]%2 == 0 and self.board[i-2][j+2] == 0:
                                    positions[(i, j)].append([(i, j), (i-1, j-1), (i-2, j+2)])
                
                # if second player, use 2 and 4
                else:

                    # if this is our piece
                    if self.board[i][j]%2 == 0 and self.board[i][j] != 0:

                        # add first diagonal and possible jump
                        if i+1 < BOARD_COLS and j+1 < BOARD_COLS:
                            if self.board[i+1][j+1] == 0:
                                positions[(i, j)].append([(i, j), (i+1, j+1)])
                            elif i+2 < BOARD_COLS and j+2 < BOARD_COLS and self.board[i+1][j+1]%2 == 1 and self.board[i+2][j+2] == 0:
                                positions[(i, j)].append([(i, j), (i+1, j+1), (i+2, j+2)])

                        # add second diagonal and possible jump
                        if i-1 >= 0 and j+1 < BOARD_COLS:
                            if self.board[i-1][j+1] == 0:
                                positions[(i, j)].append([(i, j), (i-1, j+1)])
                            elif i-2 >= 0 and j+2 < BOARD_COLS and self.board[i-1][j+1] != 0 and self.board[i-1][j+1]%2 == 1 and self.board[i-2][j+2] == 0:
                                positions[(i, j)].append([(i, j), (i-1, j+1), (i-2, j+2)])

                        # if this is our queen piece
                        if self.board[i][j] == 3:

                            # adding the two other diagonals and possible jumps
                            if i-1 >= 0 and j-1 >= 0:
                                if self.board[i-1][j-1] == 0:
                                    positions[(i, j)].append([(i, j), (i-1, j-1)])
                                elif i-2 >= 0 and j-2 >= 0 and self.board[i-1][j-1] != 0 and self.board[i-1][j-1]%2 == 0 and self.board[i-2][j-2] == 0:
                                    positions[(i, j)].append([(i, j), (i-1, j-1), (i-2, j-2)])

                            if i+1 < BOARD_COLS and j-1 >= 0:
                                if self.board[i+1][j-1] == 0:
                                    positions[(i, j)].append([(i, j), (i+1, j-1)])
                                elif i+2 < BOARD_COLS and j-2 >= 0 and self.board[i+1][j-1] != 0 and self.board[i+1][j-1]%2 == 0 and self.board[i-2][j-2] == 0:
                                    positions[(i, j)].append([(i, j), (i+1, j-1), (i+2, j-2)])

                if len(positions[(i, j)]) == 0:
                    positions.pop((i, j))

        return positions
                        
    def winner(self):
         
        # first check if Player 1 won
        if self.didPlayer1Win() == 1:
            return 1
       
        # if Player 1 didn't win then check if Player 2 won
        if self.didPlayer2Win() == 2:
            return 2
       
        # if Player 2 also didn't win then we aren't in goal state yet
        return 0
   
    # check if in goal state where Player 1 won
    def didPlayer1Win(self):
       
        for i in range(BOARD_COLS):
            for j in range(BOARD_ROWS):

                # Player 1 won if they got rid of all of Player 2's pieces
                if self.board[i][j] == 2 or self.board[i][j] == 4:
                    self.isEnd = False
                    return 0
               
        self.isEnd = True
        return 1
   
    # check if in goal state where Player 2 won
    def didPlayer2Win(self):
        for i in range(BOARD_COLS):
            for j in range(BOARD_ROWS):

                # Player 2 won if they got rid of all of Player 1's pieces
                if self.board[i][j] == 1 or self.board[i][j] == 3:
                    self.isEnd = False
                    return 0
       
        self.isEnd = True
        return 2

    def updateState(self, action):
        # action: [(x_i, y_i), (x_1, y_1) ... (x_f, y_f)]

        player = self.board[action[0]]
        pieces_taken = 0
        in_danger = 0

        for i in range(1, len(action)):
            if self.board[action[i]] != 0:
                pieces_taken += 1
            self.board[action[i]] = 0

        self.board[action[0]] = 0
        new_pos = action[-1]

        row_needed_queen = {2: 0, 1: BOARD_ROWS - 1}
        # if now a queen
        if row_needed_queen.get(player, -1) == new_pos[0]:
            self.board[new_pos] = player * 2
        else:
            self.board[new_pos] = player

        # checking danger after move
        dx = 1 if player == 1 else -1

        #TODO: consider queens and maybe multiple hops
        x_p, y_p = new_pos
        if 0 <= x_p + dx < self.board.shape[0]:
            if 0 <= y_p - 1 < self.board.shape[1]:
                if self.board[x_p + dx, y_p - 1] not in [0, player, player*2]:
                    in_danger += 1
            if 0 <= y_p + 1 < self.board.shape[1]:
                if self.board[x_p + dx, y_p + 1] not in [0, player, player*2]:
                    in_danger += 1

        # return resulting "events" to be passed to reward function
        return (self.p1 if player == 1 else self.p2,
                pieces_taken, in_danger)

    def reset(self):
        self.board = np.array([[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0],
                               [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0],
                               [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]])
        self.boardHash = None
        self.isEnd = False

    def giveReward(self, events):
        # assumes winner() returns 0 for none, 1 for p1, 2 for p2

        # gamma = lambda val: val * (self.gamma ** turn)

        win = self.winner()
        if win == 1:
            self.p1.feedReward(10)
            self.p2.feedReward(-10)
        elif win == 2:
            self.p1.feedReward(-10)
            self.p2.feedReward(10)
        else:
            # idk
            self.p1.feedReward(0.01)
            self.p2.feedReward(0.01)

            # feeds player whos turn it was 0.5 * number of pieces they took
            events[0].feedReward(events[1] * 0.5)
            # in danger
            events[0].feedReward(events[2] * -0.5)

    # two AI bots play against each other for trainig purposes
    def play(self, rounds=100):
       
        # number of episodes to train on
        num_eps = 1

        player_1 = self.p1
        player_2 = self.p2

        for _ in range(num_eps):

            # create a new game for each round
            # this reps the board
            # state = State(player_1, player_2)

            # player_1 starts
            curr_player = player_1

            # run the game
            while not self.isEnd:

                # first look at all valid moves the curr player can make
                # note: getAvailablePositions() will return a dict where 
                # each key is curr_player's pieces (rep as a tup)
                # and each of those keys map to a list of tups that piece can move to
                positions = self.getAvailablePositions(curr_player)

                if positions == {}:
                    self.isEnd = True
                    break

                # then choose an action based on our Q-learning alg
                action = curr_player.chooseAction(positions, self)

                # then update state based on the chosen action
                events = self.updateState(action)

                # assign rewards
                # this is called after every update state
                # note: giveReward() calls feedReward()
                self.giveReward(events)

                # then add state to curr_player's states
                curr_player.addStates(self.getHash())

                # swap turns
                curr_player = player_1 if curr_player == player_2 else player_2

                print(self.board)
                print()
            # reset game and run another episode
            player_1.reset()
            player_2.reset()

        # at very end of training we save policy
        # self.savePolicy()


    ############################# FOR LATER
    # def playHuman(self):
    #     # play human

    # def showBoard(self):
    #     # gui display
    



