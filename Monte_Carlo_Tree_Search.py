import copy
import random
import time
import math
# we build the monte carlo tree using nodes from this class
class Node:

    def __init__(self, parent: object = None, move: tuple = None):
        self.parent = parent
        self.move = move
        # number of times this node has been visited
        self.NumVisted = 0
        # all the nodes children
        self.children = {}
        # how good the node is
        self.reward = 0

    # defines the value of the node using the UTC formula
    # used when assesing the next selection
    def value(self):
        # a rather low explore value gotten from testing
        exploreValue = 0.6

        if self.NumVisted == 0:
            if exploreValue != 0:
                return 1000000000
            else:
                return 0
        else:
            # UTC
            return self.reward / self.NumVisted + (
                exploreValue
                * math.sqrt(2 * math.log(self.parent.NumVisted) / self.NumVisted)
            )

    # add children
    def add_to_children(self, children):
        for i in children:
            self.children[i.move] = i
        return


# MCTS class
# contains everything nessicary to explore the game using monte carlo methods
# partly adapted from https//towardsdatascience.com/monte-carlo-tree-search-implementing-reinforcement-learning-in-real-time-game-player-a9c412ebeff5
class MonteCarloTreeSearch:

    def __init__(self, game):

        self.root_state = copy.deepcopy(game)
        self.root = Node()

    # select new node to explore
    def selection(self):
        node = self.root
        state = copy.deepcopy(self.root_state)

        while len(node.children) != 0:

            children = node.children.values()

            # get the largest value in the list
            valueList = []
            for child in children:
                valueList.append(child.value())
            highestValue = max(valueList)
            # pick the nodes with the highest value
            highestNodes = []
            for child in children:
                if child.value() == highestValue:
                    highestNodes.append(child)
            max_nodes = highestNodes

            # choose one of the nodes with the highest value at random
            if len(max_nodes) > 1:
                node = random.choice(max_nodes)
            else:
                node = max_nodes[0]
            state.turn(node.move)

            # expand any unexplored children
            if node.NumVisted == 0:
                return node, state
        # make a random move
        if self.expand(node, state) == 1:
            movesList = list(node.children.values())
            node = random.choice(movesList)
            state.turn(node.move)
        return node, state

    # find all possible next moves in the tree
    def expand(self, parent, game):

        childList = []
        # do nothing if the game finished, this is very rare
        if game.find_loser() != 0:
            return -1

        else:

           


            gamecopy = copy.deepcopy(game)
            thePlayer = game.current_player
            for aMove in game.possibleMoves():
                #action removal improvement
                #removes any moves that move a player to an empty board
                gamecopy.turn(aMove)
                if thePlayer == '0':
                    playerBoard = gamecopy.board[3][0]
                else:
                    playerBoard = gamecopy.board[3][1]

                playerFlag = 0
                for y in range(0, 4):
                    for x in range(0, 4):
                        if gamecopy.board[playerBoard][y][x] == thePlayer:
                            playerFlag = 1
                            break
                if playerFlag == 1:
                    childNode = Node(parent, aMove)
                    childList.append(childNode)
                
                gamecopy = copy.deepcopy(game)

            parent.add_to_children(childList)
            return 1

    # random playout

    def roll_out(self, state, player):
        
        # loop until someone loses
        while state.find_loser() == 0:

            if state.current_player == "0":
                currentBoard = state.board[3][0]
            else:
                currentBoard = state.board[3][1]
            
            ogstate = copy.deepcopy(state)
            currentTurn = ogstate.current_player
            
            starting2 = time.time()
            #possibleMoves = state.possibleMoves()
            List = []
            playerExists = 0
            for y in range(0, 4):
                for x in range(0, 4):
                    if state.board[currentBoard][y][x] == state.current_player:
                        playerExists = 1
                        # if the peice exists then attempt all moves with that peice
                        for firstMove in range(0, 6):
                            for secondMove in range(0, 6):
                                for changeBoard in range(0, 3):
                                    List.append(                                            tuple(
                                                [firstMove, secondMove, x, y, changeBoard]
                                            ))
           
            if playerExists == 0:
                        for boardNum in range(0, 3):
                            if boardNum != currentBoard:                               
                                List.append(tuple([-9, -9, -9, -9, boardNum]))
              

            #print(possibleMoves)
            move = random.choice(List)
            #UNCOMMENT THE LINE ON THE NEXT ONE TO ACTIVATE HEAVIER PLAYOUTS
            while ogstate.a_turn(move[0],move[1],move[2],move[3],move[4]): #== -1 or ogstate.find_loser() == currentTurn:
                 ogstate = copy.deepcopy(state) 
                 List.remove(move)
                 move = random.choice(List)

            state.turn(move)
            

        return state.find_loser()

    # go back up the tree with the result
    def backpropagation(self, loser, node, player):

        # check if the loser is not the player who is searching
        if loser != player:
            # if it is give a bad score
            # should be 0
            score = 0
        else:
            score = 1
        # go all the way up the tree
        while node != None:
            node.reward += score
            node.NumVisted += 1
            # 2 player game so if current node wins, on next node that player has lost
            if score != 0:
                score = 1
            else:
                score = 0

            node = node.parent

        return

    # find the strongest move (most visited)
    def strongest_move(self):

        if self.root_state.find_loser() == 0:
            vistedList = []
            for child in self.root.children.values():
                vistedList.append(child.NumVisted)
            highestValue = max(vistedList)

            strongestChildren = []
            for child in self.root.children.values():
                if child.NumVisted == highestValue:
                    strongestChildren.append(child)

            strongestNode = random.choice(strongestChildren)

            return strongestNode.move
        # return 0 if the game is over
        else:
            return 0

    # this runs the MCTS
    def monteCarloSearch(self, numRollouts):

        for i in range(1, numRollouts):
            print(i)
            node, state = self.selection()
            player = state.current_player

            outcome = self.roll_out(state, player)

            self.backpropagation(outcome, node, player)

        return

    def updateTree(self, move):

        if move in self.root.children:
            child = self.root.children[move]
            child.parent = None
            self.root = child

            # need, to update this when the player makes a moves aswell
            self.root_state.turn(child.move)
            return

        # tree wasnt expanded enough so make a new one
        self.root_state.turn(move)
        self.root = Node()
        return

