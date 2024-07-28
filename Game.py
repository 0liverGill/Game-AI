
import copy

# the game class holds everything needed to manipulate a game
class Game:
    def __init__(self):
        # white player = 0 and black player = X
        self.current_player = "0"
        # holds the number of peices each player has
        self.white_pieces = 4
        self.black_pieces = 4

        # contains a retpresentation of the board state
        # the last part of the array contains the grid where each players next move will take place ([3][0] is white, [3][1] is black)
        self.board = [
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", "X"],
            ],
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", "X"],
            ],
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", "X"],
            ],
            [0, 2],
        ]

    # displays the current board in an ASCII format, to be used to help human players understand the current gamestate
    def display_board(self):
        print("p1 pieces", self.white_pieces, " \n")
        if self.board[3][0] == 0:
            print("            p1 \n")
        elif self.board[3][0] == 1:
            print("                                           p1 \n")
        elif self.board[3][0] == 2:
            print(
                "                                                                          p1 \n"
            )
        print(
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----| \n"
            "| ",
            self.board[0][0][0],
            " | ",
            self.board[0][0][1],
            " | ",
            self.board[0][0][2],
            " | ",
            self.board[0][0][3],
            " |      " "| ",
            self.board[1][0][0],
            " | ",
            self.board[1][0][1],
            " | ",
            self.board[1][0][2],
            " | ",
            self.board[1][0][3],
            " |      " "| ",
            self.board[2][0][0],
            " | ",
            self.board[2][0][1],
            " | ",
            self.board[2][0][2],
            " | ",
            self.board[2][0][3],
            " | \n"
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----| \n"
            "| ",
            self.board[0][1][0],
            " | ",
            self.board[0][1][1],
            " | ",
            self.board[0][1][2],
            " | ",
            self.board[0][1][3],
            " |      " "| ",
            self.board[1][1][0],
            " | ",
            self.board[1][1][1],
            " | ",
            self.board[1][1][2],
            " | ",
            self.board[1][1][3],
            " |      " "| ",
            self.board[2][1][0],
            " | ",
            self.board[2][1][1],
            " | ",
            self.board[2][1][2],
            " | ",
            self.board[2][1][3],
            " | \n"
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----| \n"
            "| ",
            self.board[0][2][0],
            " | ",
            self.board[0][2][1],
            " | ",
            self.board[0][2][2],
            " | ",
            self.board[0][2][3],
            " |      " "| ",
            self.board[1][2][0],
            " | ",
            self.board[1][2][1],
            " | ",
            self.board[1][2][2],
            " | ",
            self.board[1][2][3],
            " |      " "| ",
            self.board[2][2][0],
            " | ",
            self.board[2][2][1],
            " | ",
            self.board[2][2][2],
            " | ",
            self.board[2][2][3],
            " | \n"
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----| \n"
            "| ",
            self.board[0][3][0],
            " | ",
            self.board[0][3][1],
            " | ",
            self.board[0][3][2],
            " | ",
            self.board[0][3][3],
            " |      " "| ",
            self.board[1][3][0],
            " | ",
            self.board[1][3][1],
            " | ",
            self.board[1][3][2],
            " | ",
            self.board[1][3][3],
            " |      " "| ",
            self.board[2][3][0],
            " | ",
            self.board[2][3][1],
            " | ",
            self.board[2][3][2],
            " | ",
            self.board[2][3][3],
            " | \n"
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----|      "
            "|-----|-----|-----|-----| \n",
        )

        if self.board[3][1] == 0:
            print("            p2 \n")
        elif self.board[3][1] == 1:
            print("                                           p2 \n")
        elif self.board[3][1] == 2:
            print(
                "                                                                          p2 \n"
            )
        print("p2 pieces", self.black_pieces, " \n")

    # this function creates lets a human player make a move via command line input
    def player_move(self):
        # input the loaction of the piece to move
        y = int(input("enter Y: "))
        x = int(input("enter X: "))
        pushType = -1
        # enter the first move
        while True:
            print(
                "controls: wasd for up down left right, b for move to right board, f for move to left board"
            )
            direction = input("Enter Direction: ")
            if direction == "w":
                pushType = 0
                break
            elif direction == "s":
                pushType = 1
                break
            elif direction == "a":
                pushType = 2
                break
            elif direction == "d":
                pushType = 3
                break
            elif direction == "b":
                pushType = 4
                break
            elif direction == "f":
                pushType = 5
                break
        while True:
            print(
                "controls: wasd for up down left right, b for move to right board, f for move to left board"
            )

            secondDirection = input("Enter Second Direction: ")
            if secondDirection == "w":
                secondPushType = 0
                break
            elif secondDirection == "s":
                secondPushType = 1
                break
            elif secondDirection == "a":
                secondPushType = 2
                break
            elif secondDirection == "d":
                secondPushType = 3
                break
            elif secondDirection == "b":
                secondPushType = 4
                break
            elif secondDirection == "f":
                secondPushType = 5
                break

        newBoard = -1
        while True:
            boardInput = input("Enter Valid New Board (left to right: 0,1 or 2): ")
            if boardInput == "0":
                newBoard = 0
                break
            if boardInput == "1":
                newBoard = 1
                break
            if boardInput == "2":
                newBoard = 2
                break
        # make the turn
        theTurn = tuple([pushType, secondPushType, x, y, newBoard])
        self.turn(theTurn)
        # return the move made
        return theTurn

    def turn(self, moveTuple):
        # if it is whites turn
        if self.current_player == "0":
            # make move
            self.a_turn(
                moveTuple[0], moveTuple[1], moveTuple[2], moveTuple[3], moveTuple[4]
            )
            # then switch player
            self.current_player = "X"
        else:
            self.a_turn(
                moveTuple[0], moveTuple[1], moveTuple[2], moveTuple[3], moveTuple[4]
            )
            self.current_player = "0"

        return

    # responsible for moving a peice on the board
    def move(self, pushType, xPos, yPos):
        # pushType: 0 = up, 1 = down, 2 = left, 3 = right, 4 = time back, 5 = time forwards
        if self.current_player == "0":
            currentBoard = self.board[3][0]
        else:
            currentBoard = self.board[3][1]
        # push up
        if pushType == 0:

            # if nothing to push into then ignore it (its dead)
            if yPos != 0:

                if self.board[currentBoard][yPos - 1][xPos] != " ":

                    # if they are the same thing (two player tokens) then you cant move into them
                    if (
                        self.board[currentBoard][yPos - 1][xPos]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        return -1, -1

                    # otherwise push it along
                    else:
                        # recursivley call the push function incase they are now pushing into something else (chain reaction)

                        self.push_object(0, xPos, yPos - 1)
                        self.board[currentBoard][yPos - 1][xPos] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "
                # if the player is moving into nothing then skip above  steps (nothing to push)
                else:
                    self.board[currentBoard][yPos - 1][xPos] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:
                # cannot move this way so state is invalid
                return -1, -1
            # update the objects position
            yPos = yPos - 1

        # push down
        elif pushType == 1:

            if yPos != 3:

                if self.board[currentBoard][yPos + 1][xPos] != " ":

                    if (
                        self.board[currentBoard][yPos + 1][xPos]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        return -1, -1

                    else:

                        self.push_object(1, xPos, yPos + 1)
                        self.board[currentBoard][yPos + 1][xPos] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "

                else:
                    # this time we go down instead of up (+1)
                    self.board[currentBoard][yPos + 1][xPos] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:

                return -1, -1

            yPos = yPos + 1

            # push left
        elif pushType == 2:

            if xPos != 0:

                if self.board[currentBoard][yPos][xPos - 1] != " ":

                    if (
                        self.board[currentBoard][yPos][xPos - 1]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        return -1, -1

                    else:

                        self.push_object(2, xPos - 1, yPos)
                        self.board[currentBoard][yPos][xPos - 1] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "

                else:

                    self.board[currentBoard][yPos][xPos - 1] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:

                return -1, -1
            xPos = xPos - 1

        # push right
        elif pushType == 3:

            if xPos != 3:

                if self.board[currentBoard][yPos][xPos + 1] != " ":

                    if (
                        self.board[currentBoard][yPos][xPos + 1]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        return -1, -1

                    else:

                        self.push_object(3, xPos + 1, yPos)
                        self.board[currentBoard][yPos][xPos + 1] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "

                else:

                    self.board[currentBoard][yPos][xPos + 1] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:

                return -1, -1

            xPos = xPos + 1
        # time travel backwards
        elif pushType == 4:

            if self.current_player == "0":
                numPieces = self.white_pieces
            else:
                numPieces = self.black_pieces
            if currentBoard != 2 and numPieces > 0:

                if self.board[currentBoard + 1][yPos][xPos] != " ":

                    return -1, -1

                else:

                    # dont need to add empty space beacuse copy is created
                    self.board[currentBoard + 1][yPos][xPos] = self.board[currentBoard][
                        yPos
                    ][xPos]

                    # change the current board
                    # we also used a piece to time travel backwards
                    if self.current_player == "0":
                        self.board[3][0] += 1
                        self.white_pieces -= 1
                    else:
                        self.board[3][1] += 1
                        self.black_pieces -= 1

            else:

                return -1, -1

        # time travel forwards
        elif pushType == 5:

            if currentBoard != 0:

                if self.board[currentBoard - 1][yPos][xPos] != " ":

                    return -1, -1

                else:

                    self.board[currentBoard - 1][yPos][xPos] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "
                    if self.current_player == "0":
                        self.board[3][0] -= 1

                    else:
                        self.board[3][1] -= 1

            else:

                return -1, -1
        return yPos, xPos

    # pushing an object into another object is *slightly different because if you push a player into themselves they are both destroyed
    # this makes it slightly more efficent to create a new function for it rather than deal with the overhead (increased game states) by reusing 'move()'
    # while it does reduce cohesion of the code, I feel it is necessary becuase of the many evaluations.
    def push_object(self, pushType, xPos, yPos):
        # pushType: 0 = up, 1 = down, 2 = left, 3 = right, 4 = time back, 5 = time forwards

        if self.current_player == "0":
            currentBoard = self.board[3][0]
        else:
            currentBoard = self.board[3][1]
        # push up
        if pushType == 0:

            # if nothing to push into then ignore it (its dead)
            if yPos != 0:

                if self.board[currentBoard][yPos - 1][xPos] != " ":

                    # if they are the same thing (two player tokens) then destroy both of them
                    if (
                        self.board[currentBoard][yPos - 1][xPos]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        self.board[currentBoard][yPos - 1][xPos] = " "
                        self.board[currentBoard][yPos][xPos] = " "

                    # otherwise push it along
                    else:
                        # recursivley call the push function incase they are now pushing into something else (chain reaction)

                        self.push_object(0, xPos, yPos - 1)
                        self.board[currentBoard][yPos - 1][xPos] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "
                # if the player is moving into nothing then skip above  steps (nothing to push)
                else:
                    self.board[currentBoard][yPos - 1][xPos] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:
                # cannot move this way so state is invalid
                return -1, -1
            # update the objects position
            yPos = yPos - 1

        # push down
        elif pushType == 1:

            if yPos != 3:

                if self.board[currentBoard][yPos + 1][xPos] != " ":

                    if (
                        self.board[currentBoard][yPos + 1][xPos]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        self.board[currentBoard][yPos + 1][xPos] = " "
                        self.board[currentBoard][yPos][xPos] = " "

                    else:

                        # self.push_object(self.board,currentBoard,yPos+1,xPos,1)
                        self.push_object(1, xPos, yPos + 1)
                        self.board[currentBoard][yPos + 1][xPos] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "

                else:
                    # this time we go down instead of up (+1)
                    self.board[currentBoard][yPos + 1][xPos] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:

                return -1, -1

            yPos = yPos + 1

            # push left
        elif pushType == 2:

            if xPos != 0:

                if self.board[currentBoard][yPos][xPos - 1] != " ":

                    if (
                        self.board[currentBoard][yPos][xPos-1]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        self.board[currentBoard][yPos][xPos-1] = " "
                        self.board[currentBoard][yPos][xPos] = " "

                    else:

                        self.push_object(2, xPos - 1, yPos)
                        self.board[currentBoard][yPos][xPos - 1] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "

                else:

                    self.board[currentBoard][yPos][xPos - 1] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:

                return -1, -1
            xPos = xPos - 1

        # push right
        elif pushType == 3:

            if xPos != 3:

                if self.board[currentBoard][yPos][xPos + 1] != " ":

                    if (
                        self.board[currentBoard][yPos][xPos+1]
                        == self.board[currentBoard][yPos][xPos]
                    ):
                        self.board[currentBoard][yPos][xPos+1] = " "
                        self.board[currentBoard][yPos][xPos] = " "

                    else:

                        self.push_object(3, xPos + 1, yPos)
                        self.board[currentBoard][yPos][xPos + 1] = self.board[
                            currentBoard
                        ][yPos][xPos]
                        self.board[currentBoard][yPos][xPos] = " "

                else:

                    self.board[currentBoard][yPos][xPos + 1] = self.board[currentBoard][
                        yPos
                    ][xPos]
                    self.board[currentBoard][yPos][xPos] = " "

            else:

                return -1, -1

            xPos = xPos + 1
       
        return yPos, xPos

    # checks if someone has lost the game
    # if someone has lost returns the char of the losers peices
    # otherwise returns zero
    def find_loser(self):
        loser = 0

        for player in ["0", "X"]:
            # this method doesnt nessisarily need to check all boards
            if (
                player not in self.board[0][0]
                and player not in self.board[0][1]
                and player not in self.board[0][2]
                and player not in self.board[0][3]
            ):
                # nothing in board 0 so check board 1
                if (
                    player not in self.board[1][0]
                    and player not in self.board[1][1]
                    and player not in self.board[1][2]
                    and player not in self.board[1][3]
                ):
                    # if nothing in board 1 then that player loses
                    return player
                # player is in board 1 but not 0
                else:
                    if (
                        player not in self.board[2][0]
                        and player not in self.board[2][1]
                        and player not in self.board[2][2]
                        and player not in self.board[2][3]
                    ):
                        return player
            # player is in board 1

            elif (
                player not in self.board[1][0]
                and player not in self.board[1][1]
                and player not in self.board[1][2]
                and player not in self.board[1][3]
            ):
                if (
                    player not in self.board[2][0]
                    and player not in self.board[2][1]
                    and player not in self.board[2][2]
                    and player not in self.board[2][3]
                ):
                    return player

        return loser

    # function use to switch to a board of choosing, newBoard is the number of the current board
    def changeBoard(self, newBoard):
        if self.current_player == "0":
            if newBoard >= 0 and newBoard <= 2:
                self.board[3][0] = newBoard
            else:
                return -1
        else:
            if newBoard >= 0 and newBoard <= 2:
                self.board[3][1] = newBoard
            else:
                return -1

    # a players turn consists of two moves followed by switching boards
    def a_turn(self, firstMove, secondMove, x, y, newBoard):
        if self.current_player == "0":
            originalBoard = self.board[3][0]
        else:
            originalBoard = self.board[3][1]
        if newBoard == originalBoard:
            return -1
        # if no moves can be made then indicate with "-9"
        if firstMove == -9 and secondMove == -9:
            self.changeBoard(newBoard)
            return 0
        # make the first move
        newY, newX = self.move(firstMove, x, y)

        if newY != -1:

            # make the second move
            finalX, finalY = self.move(secondMove, newX, newY)
            if finalX != -1:
                # move player to new board
                if self.changeBoard(newBoard) == -1:
                    return -1
            else:

                return -1
        # return -1 if move cannot be made
        else:
            return -1

        return 0

    def possibleMoves(self):

        if self.current_player == "0":
            currentBoard = self.board[3][0]
        else:
            currentBoard = self.board[3][1]

        possibleMoves = []
     

        # we create a copy of the board to reset the board to after each loop
        originalBoard = copy.deepcopy(self.board)

        # originalPlayer =  self.current_player

        # originalWhiteBoard = self.board[3][0]
        originalWhitePieces = self.white_pieces

        # originalBlackBoard = self.current_black_board
        # originalBlackPieces = self.board[3][1]
        originalBlackPieces = self.black_pieces

        playerExists = 0
        for y in range(0, 4):
            for x in range(0, 4):
                if self.board[currentBoard][y][x] == self.current_player:
                    playerExists = 1
                    for firstMove in range(0, 6):
                        for secondMove in range(0, 6):
                            for changeBoard in range(0, 3):

                                if (
                                    self.a_turn(
                                        firstMove, secondMove, x, y, changeBoard
                                    )
                                    != -1
                                ):
                                    #print(self.current_player)
                                        possibleMoves.append(
                                            tuple(
                                                [firstMove, secondMove, x, y, changeBoard]
                                            )
                                        )

                                # reset board for the next state
                                self.board = copy.deepcopy(originalBoard)

                                # self.current_player= originalPlayer
                                # self.board[3][0] = originalWhiteBoard
                                self.white_pieces = originalWhitePieces
                                self.black_pieces = originalBlackPieces
                                # self.board[3][1] = originalBlackPieces

        if playerExists == 0:
            for boardNum in range(0, 3):
                if boardNum != currentBoard:
                    possibleMoves.append(tuple([-9, -9, -9, -9, boardNum]))
                    self.board = originalBoard
                    # self.current_player= originalPlayer
                    # self.board[3][0] = originalWhiteBoard
                    self.white_pieces = originalWhitePieces
                    self.black_pieces = originalBlackPieces

        return possibleMoves

    # method returns all the possible successor states to a gamestate
    def successors(self):

        if self.current_player == "0":
            currentBoard = self.board[3][0]
        else:
            currentBoard = self.board[3][1]

        possibleMoves = []

        # we create a copy of the board to reset the board to after each loop
        originalSelf = copy.deepcopy(self)

        # loop the board until a players peice is found
        playerExists = 0
        for y in range(0, 4):
            for x in range(0, 4):
                if self.board[currentBoard][y][x] == self.current_player:
                    playerExists = 1
                    # if the peice exists then attempt all moves with that peice
                    for firstMove in range(0, 6):
                        for secondMove in range(0, 6):
                            for changeBoard in range(0, 3):

                                if (
                                    self.a_turn(
                                        firstMove, secondMove, x, y, changeBoard
                                    )
                                    != -1
                                ):
                                    # the move is valid so we change the current player
                                    # then add the state to the list of successors
                                    if self.current_player == "0":
                                        self.current_player = "X"
                                    else:
                                        self.current_player = "0"

                                    possibleMoves.append(copy.deepcopy(self))

                                self = copy.deepcopy(originalSelf)

        # if there are no pieces on this board then make no move and just switch boards
        if playerExists == 0:
            for boardNum in range(0, 3):
                if boardNum != currentBoard:
                    self.changeBoard(boardNum)
                    if self.current_player == "0":
                        self.current_player = "X"
                    else:
                        self.current_player = "0"
                    game = copy.deepcopy(self)
                    possibleMoves.append(game)
                    self = copy.deepcopy(originalSelf)

        # optimisation to reduce the number of gamestates
        # looks for duplicate gamestates and removes them
        # can reduce number of successors by up to 25%!
        possibleMoves2 = []
        boards = []
        for item in possibleMoves:
            if item.board not in boards:
                possibleMoves2.append(item)
                boards.append(item.board)

        return possibleMoves2, self
