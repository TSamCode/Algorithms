# python implementation for a 2x3 grid world to consider Q-learning
# The only cells with rewards are Cell[0,2] = 16, Cell [1,2] = 20
# We will count the indices from the upper right corner, this is to be consistent with indices in numpy arrays

import numpy as np

#Global parameters
rows = 2
cols = 3
startState = [1,0]
rewards = np.array([[0,0,16], [0,0,-16]])
winningState = [0,2]
losingState = [1,2]

class Board():
    
    def __init__(self, state = startState):
        self.grid = np.zeros([rows, cols])
        self.state = state
        self.terminated = False

    def reward(self):
        return rewards[self.state[0]][self.state[1]]

    def terminatedFunc(self):
        if (self.state == winningState) or (self.state == losingState):
            self.terminated = True
        else:
            self.terminated = False

    def move(self, action):
        """
        we can move up, down, left, right in any grid apart from the winning or losing states which are absorbing
        """
        
        currentState = self.state

        if action == "up":
            newState = (self.state[0] - 1, self.state[1])
        elif action == "down":
            newState = (self.state[0] + 1, self.state[1])
        elif action == "right":
            newState = (self.state[0], self.state[1] + 1)
        elif action == "left":
            newState = (self.state[0], self.state[1] - 1)
        else:
            raise NameError(action, 'This is not a valid action!')

        # Need to check if the new state is a legal move
        if (newState[0] >= 0) & (newState[0] <= 1) & (newState[1] >= 0) & (newState[1] <= 2):
            return newState
        else:
            print('This move takes you off the board, you have not moved!')
            return currentState

    def printGrid(self):
        for i in range(rows):
            print("-------------------")
            rowFormat = '|'
            for j in range(cols):
                if rewards[i][j] != 0:
                    item = str(reward[i][j])
                rowFormat += item + '|'
            print(rowFormat)
        print("-------------------")

class Agent():

    def __init__(self):
        self.states = []
        self.actions = ['up', 'down', 'left', 'right']
        self.Board = Board()
        self.terminated = self.Board.terminated
        self.alpha = 0.5
        self.gamma = 0.75
        self.epsilon = 0.1

        # We need to create a dictionary of Q-values
        self.qValues = {}
        for i in range(rows):
            for j in range(cols):
                # At each position on the board we need to create a dictionary to hold the q-values for the actions at that state
                # This will then gives us Q-values for all the state-action pairs Q(s,a) - initialised to zero
                self.qValues[[i,j]] = {}
                for action in self.actions:
                    self.qValues[[i,j]][action] = 0

    def pickAction(self):
        
        # We define a maxReward parameter to track the highest reward of the possible actions from that state
        maxReward = 0

        # If the randNo is within epsilon then we pick a random move to explore the board
        if np.random.uniform(0,1) <= self.epsilon:
            nextAction = np.random.choice(self.actions)
        # If we are not ecploring then we will pick the action with the best expected reward
        else:
            for action in self.actions:
                currentState = self.Board.state
                expectedReward = self.qValues[currentState][action]
                if expectedReward >= maxReward:
                    nextAction = action
                    maxReward = expectedReward
                
        return nextAction

    def takeAction(self, action):
        newState = self.Board.move(action)
        return Board(state = newState)

    def resetAgent(self):
        self.states = []
        self.Board = Board()
        self.terminated = self.Board.terminated

    def beginGridWorld(self, iter = 10):
        i = 0
        while i < iter:
            # When we get to the end of the game we back propagate the rewards through the grid
            if self.Board.terminated:
                reward = self.Board.reward()
                for action in self.actions:
                    self.qValues[self.Board.state][action] = reward
                print("Game terminated with reward: {}".format(reward))

                for state in reversed(self.states):
                    # state[0] gives us the state and state[1] gives us the action
                    # We are now working in reverse back through the state, action pairs that were performed
                    currentQValue = self.qValues[state[0]][state[1]]
                    
                    # As we move back through the states we are then changing the reward to effectively be the best estimate of Q for the state ahead of it
                    reward = currentQValue + self.alpha * (self.gamma * reward - currentQValue)
                    self.qValues[state[0]][state[1]] = round(reward, 3)
                
                # Once we have finished the game we need to clear all information before beginning the next iteration
                self.resetAgent()
                i += 1

            # If the game is not over we need to take another action
            else:
                # We need to first decide what action we will take and add the state, action pair to the list of states and action already taken
                action = self.pickAction()
                self.states.append([self.Board.state ,action])
                print("The current state is {}, and the action taken will be {}".format(self.Board.state, action))
                # We then need to actually take the action to move the state of the board
                self.Board = self.takeAction(action)
                # We then need to work out if the game has ended or not
                self.Board.terminatedFunc()
                print("The next state is {}".format(self.Board.state))
                print("-------------------------")
                self.terminated = self.Board.terminated
