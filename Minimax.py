import random
import copy
# all things minimax related go here
class MINIMAX:
    def __init__(self,AIplayer, heuristic):
        self.AIplayer = AIplayer
        self.heuristic = heuristic
        

    # based on number of boards a player has peices on
    def heuristic1(self,state):

        count = 0

        for a in range(0, 3):
            breakFlag = 0
            for b in range(0, 4):
                for c in range(0, 4):
                    if state.board[a][b][c] == self.AIplayer:
                        count += 1
                        breakFlag = 1
                        break
                if breakFlag == 1:
                    break

        if self.AIplayer == "0":
            otherPlayer = "X"
        else:
            otherPlayer = "0"

        for a in range(0, 3):
            breakFlag = 0
            for b in range(0, 4):
                for c in range(0, 4):
                    if state.board[a][b][c] == otherPlayer:
                        count -= 1
                        breakFlag = 1
                        break
                if breakFlag == 1:
                    break
        return count

    # based on number of peices a player has
    def heuristic2(self,state):
        count = 0
        count2 = 0

        for a in range(0, 3):
            for b in range(0, 4):
                for c in range(0, 4):
                    if state.board[a][b][c] == self.AIplayer:

                        count += 1
        # add peices depending on player assesing
        if self.AIplayer == "0":
            count += state.white_pieces
            otherPlayer = "X"
        else:
            count += state.black_pieces
            otherPlayer = "0"

        for a in range(0, 3):
            for b in range(0, 4):
                for c in range(0, 4):
                    if state.board[a][b][c] == otherPlayer:

                        count2 += 1

        if self.AIplayer == "0":
            count2 += state.black_pieces
        else:
            count2 += state.white_pieces
        return count - count2

    # based on number of peices a player has and thier position in the game
    def heuristic3(self,state):
        count = 0
        count2 = 0

        for a in range(0, 3):
            for b in range(0, 4):
                for c in range(0, 4):
                    if state.board[a][b][c] == self.AIplayer:
                        count += 1
                        # add a small score bonus if the peice is closer to the center
                        if (c > 0 and c < 3) and (b > 0 and b < 3):
                            count += 0.05
                        elif (
                            (c == 0 and b == 0)
                            or (c == 0 or b == 3)
                            or (c == 3 and b == 0)
                            or (c == 3 and b == 3)
                        ):
                            pass
                        else:
                            count + 0.01

        if self.AIplayer == "0":
            count += state.white_pieces
            otherPlayer = "X"
        else:
            count += state.black_pieces
            otherPlayer = "0"

        for a in range(0, 3):
            for b in range(0, 4):
                for c in range(0, 4):
                    if state.board[a][b][c] == otherPlayer:
                        count2 += 1
                        if (c > 0 and c < 3) and (b > 0 and b < 3):
                            count2 += 0.05
                        elif (
                            (c == 0 and b == 0)
                            or (c == 0 or b == 3)
                            or (c == 3 and b == 0)
                            or (c == 3 and b == 3)
                        ):
                            pass
                        else:
                            count2 + 0.01
        if self.AIplayer == "0":
            count2 += state.black_pieces
        else:
            count2 += state.white_pieces
        return count - count2

    # minimax algoritm via recursion
    def minimax(self,depth,alpha,beta,maxPlayer,state):

        # recursion ends here if the game is over
        loser = state.find_loser()
        # someone has lost so return the ocr
        if loser == '0' or loser == 'X':
            
            if loser == self.AIplayer:
                
                return -50
            else:
               
                return 50
        # recursion ends here if the depth limit is reached
        if depth == 0 or loser != 0:
            # evaluate depending on heuristic
            if self.heuristic == 1:
                return self.heuristic1(state)
            elif self.heuristic == 2:

                return self.heuristic2(state)
            elif self.heuristic == 3:

                return self.heuristic3(state)
        # this player is trying to maximize the score
        if maxPlayer == 1:
            largestEvaluation = -10000
            temp = copy.deepcopy(state)
            children, current = temp.successors()
            state = current

            for child in children:
                evaluation = self.minimax(
                    depth-1,alpha,beta,0,child
                )
                largestEvaluation = max(largestEvaluation, evaluation)
                alpha = max(alpha, evaluation)
                # we do a little pruning
                if beta <= alpha:
                    break

            return largestEvaluation
        # otherwise we are minimizing the score
        else:
            smallestEvaluation = 10000
            temp = copy.deepcopy(state)
            children, current = temp.successors()
            state = current

            for child in children:
                evaluation = self.minimax(
                    depth-1,alpha,beta,1,child
                )
                smallestEvaluation = min(smallestEvaluation, evaluation)
                
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break

            return smallestEvaluation

    # applys minimax then picks the best move
    def pick_minimax_move(self, Inputstate, depth):
        #we do this to account for the depth input
        #essentially makes depth input more accurate
        depth = depth-1

            
        originalState = copy.deepcopy(Inputstate)
        newState = copy.deepcopy(Inputstate)

        children, current = Inputstate.successors()
        Inputstate = current
        # minimax
        value_moves = [
            (self.minimax(depth, -1000, 1000, 0,theState), theState)
            for theState in children
        ]

        # picks best state
        valueList = []
        for pmove in value_moves:
            valueList.append(pmove[0])
        highestValue = max(valueList)
        print("maximum")
        print(highestValue)
        highestValueList = []
        for p2move in value_moves:
            if p2move[0] == highestValue:
                highestValueList.append(p2move)
        bestMove = random.choice(highestValueList)

        # translates the new state into a move
        for move in newState.possibleMoves():
            newState.turn(move)

            if newState.board == bestMove[1].board:
                # if newState.board == bestMove[1].board:
                if (newState.white_pieces == bestMove[1].white_pieces) and (
                    newState.black_pieces == bestMove[1].black_pieces
                ):
                    print("minimax move:")
                    print(move)
                    return move
            newState = copy.deepcopy(originalState)

        # this should never be reached
        return -1
