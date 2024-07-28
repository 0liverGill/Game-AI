import Game
import Minimax
import Monte_Carlo_Tree_Search as MCTS
import copy
import time
# all simulations are run through this class
class Test:
    def __init__(self):
        self.game = Game.Game()

    def reset_game(self):
        self.game = Game.Game()


    def call_minimax(self,minimaxNo,depth):
        gameCopy = copy.deepcopy(self.game)
        minimaxMove = minimaxNo.pick_minimax_move(gameCopy, depth)
        self.game.turn(minimaxMove)
        self.game.display_board()
    def minimax_VS_minimax(self, depth, heuristic1, heuristic2):
        minimax1 = Minimax.MINIMAX("0",heuristic1)
        minimax2 = Minimax.MINIMAX("X",heuristic2)
        noMoves1 = 0
        noMoves2 = 0
        minimaxTotalTime1 = 0
        minimaxTotalTime2 = 0
        # game loop
        while True:

            # minimax1
            minimaxStart = time.time()
            self.call_minimax(minimax1,depth)
            # collect variouse data
            print("time")
            print(time.time() - minimaxStart)
            minimaxTotalTime1 += time.time() - minimaxStart
            noMoves1 += 1
            # end the loop if the game is over
            if self.game.find_loser() != 0:
                print("gameover")
                break

            # minimax2
            minimaxStart = time.time()
            self.call_minimax(minimax2,depth)
            print("time")
            print(time.time() - minimaxStart)
            minimaxTotalTime2 += time.time() - minimaxStart
            noMoves2 += 1
            if self.game.find_loser() != 0:
                print("gameover")
                break
        # calculate averages
        totalMoves = noMoves1 + noMoves2
        averageTime1 = minimaxTotalTime1 / noMoves1
        averageTime2 = minimaxTotalTime2 / noMoves2
        # print this data to the screen
        print("total moves")
        print(totalMoves)
        print("average time 1")
        print(averageTime1)
        print("average time 2")
        print(averageTime2)
        # return the data to be later recorded
        return self.game.find_loser(), totalMoves, averageTime1, averageTime2

    def MonteCarlo_VS_minimax(self, depth, heuristic1, rolloutAmount):
        agent = MCTS.MonteCarloTreeSearch(self.game)
        minimax = Minimax.MINIMAX("X",heuristic1)
        MCTSmoves = 0
        minimaxMoves = 0
        timetaken = 0
        minimaxTotalTime2 = 0
        self.game.display_board()
        while True:

            MCTSStart = time.time()
            agent.monteCarloSearch(rolloutAmount)

            print("best move:")
            bestMove = agent.strongest_move()
            print(bestMove)
            self.game.turn(bestMove)
            self.game.display_board()
            MCTSmoves += 1
            timetaken += time.time() - MCTSStart

            if self.game.find_loser() != 0:

                print("gameover")
                break
            agent.updateTree(bestMove)

            minimaxStart = time.time()
            gamecopy = copy.deepcopy(self.game)
            minimaxMove = minimax.pick_minimax_move(gamecopy, depth)
            # game = minimaxMove
            self.game.turn(minimaxMove)
            print("minimove")
            self.game.display_board()
            minimaxTotalTime2 += time.time() - minimaxStart
            minimaxMoves += 1
            if self.game.find_loser() != 0:
                print("gameover")
                break

            agent.updateTree(minimaxMove)
            # game.player_move(agent)
        totalMoves = MCTSmoves + minimaxMoves
        averageTime2 = minimaxTotalTime2 / minimaxMoves
        averageMctsTime = timetaken / MCTSmoves
        return self.game.find_loser(), totalMoves, averageMctsTime, averageTime2

    def human_vs_MINIMAX(self,heuristic1,depth):
        

        minimax1 = Minimax.MINIMAX("0",heuristic1)

        noMoves1 = 0
        noMoves2 = 0
        minimaxTotalTime1 = 0
        # game loop
        while True:

            # minimax1
            minimaxStart = time.time()
            gameCopy = copy.deepcopy(self.game)
            minimaxMove = minimax1.pick_minimax_move(gameCopy, depth)
            self.game.turn(minimaxMove)
            self.game.display_board()
            # collect variouse data
            minimaxTotalTime1 += time.time() - minimaxStart
            noMoves1 += 1
            # end the loop if the game is over
            if self.game.find_loser() != 0:
                print("gameover")
                break

            #player move
            playerMove = self.game.player_move()
            #self.game.turn(playerMove)
            self.game.display_board()
            noMoves2 += 1
            if self.game.find_loser() != 0:
                print("gameover")
                break
        # calculate averages
        totalMoves = noMoves1 + noMoves2
        averageTime1 = minimaxTotalTime1 / noMoves1
        # print this data to the screen
        print("total moves")
        print(totalMoves)
        print("average time 1")
        print(averageTime1)
        # return the data to be later recorded
        return self.game.find_loser(), totalMoves, averageTime1, 0

    def human_vs_MCTS(self,rolloutAmount):
        

        agent = MCTS.MonteCarloTreeSearch(self.game)
       
        MCTSmoves = 0
        playerMoves = 0
        timetaken = 0
        minimaxTotalTime2 = 0
        self.game.display_board()
        while True:

            MCTSStart = time.time()
            rolloutAmount = int(input("ENTER ROLLOUT AMOUNT: "))
            agent.monteCarloSearch(rolloutAmount)

            print("best move:")
            bestMove = agent.strongest_move()
            print(bestMove)
            self.game.turn(bestMove)
            self.game.display_board()
            MCTSmoves += 1
            timetaken += time.time() - MCTSStart

            if self.game.find_loser() != 0:

                print("gameover")
                break
            agent.updateTree(bestMove)

            playerMove = self.game.player_move()
            #self.game.turn(playerMove)
            self.game.display_board()

            playerMoves += 1
            if self.game.find_loser() != 0:
                print("gameover")
                break

            agent.updateTree(playerMove)
            # game.player_move(agent)
        totalMoves = MCTSmoves + playerMoves
        averageMctsTime = timetaken / MCTSmoves
        return self.game.find_loser(), totalMoves, averageMctsTime, 0
    

    # this allows testing an algorithm against a set puzzle
    def puzzle_minimax(self, depth, heuristic1):

        

        # list of puzzles are below, programmer must uncomment the puzzles they want to run
        """
        ########PUZZLE 1
        self.game.board = [ [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ','X',' ','0']]   ,[['0',' ',' ',' '],[' ',' ',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']]    
                 ,[[' ',' ',' ',' '],[' ','0',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']], [1,0] ]
        answer1 = [ [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','X']]   ,[['0',' ',' ',' '],[' ',' ',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']]    
                 ,[[' ',' ',' ',' '],[' ','0',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']], [1,1] ]   
        answer2 = [ [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','X']]   ,[['0',' ',' ',' '],[' ',' ',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']]    
                 ,[[' ',' ',' ',' '],[' ','0',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']], [1,2] ]
        self.game.current_player = 'X'
        ##############
        """
        ########PUZZLE 2
        self.game.board = [
            [
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", "X", " ", "0"],
            ],
            [
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " "],
                [" ", "0", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [1, 0],
        ]
        answer1 = [
            [
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", "X"],
            ],
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " "],
                [" ", "0", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [1, 1],
        ]
        answer2 = [
            [
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", "X"],
            ],
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " "],
                [" ", "0", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [1, 2],
        ]
        self.game.current_player = "X"
        minimax = Minimax.MINIMAX(self.game.current_player,heuristic1)
        ##############

        # run the algorithm on the puzzle
        self.game.display_board()
        gameCopy = copy.deepcopy(self.game)
        minimaxMove = minimax.pick_minimax_move(gameCopy, depth)
        self.game.turn(minimaxMove)
        self.game.display_board()

        # print return if the puzzle was solved correctly or not
        if self.game.board == answer1 or self.game.board == answer2:
            print("CORRECT")
            return "CORRECT"
        else:
            print("INCORRECT")
            return "INCORRECT"

    # puzzles but for MCTS
    def puzzle_MCTS(self, rollouts):

        
        ########PUZZLE 1
        
        self.game.board = [
            [
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", "X", " ", "0"],
            ],
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " "],
                [" ", "0", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [1, 0],
        ]
        answer1 = [
            [
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", "X"],
            ],
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " "],
                [" ", "0", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [1, 1],
        ]
        answer2 = [
            [
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                [" ", " ", " ", "X"],
            ],
            [
                ["0", " ", " ", " "],
                [" ", " ", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " "],
                [" ", "0", " ", "X"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
            ],
            [1, 2],
        ]
        self.game.current_player = "X"
        ##############
        
        
        """
        ########PUZZLE 2
        self.game.board = [ [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ','X',' ','0']]   ,[[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]    
                 ,[[' ',' ',' ',' '],[' ','0',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']], [1,0] ]
        answer1 = [ [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','X']]   ,[['0',' ',' ',' '],[' ',' ',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']]    
                 ,[[' ',' ',' ',' '],[' ','0',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']], [1,1] ]   
        answer2 = [ [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','X']]   ,[['0',' ',' ',' '],[' ',' ',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']]    
                 ,[[' ',' ',' ',' '],[' ','0',' ','X'],[' ',' ',' ',' '],[' ',' ',' ',' ']], [1,2] ]
        self.game.current_player = 'X'
        
        ##############
        """

        agent = MCTS.MonteCarloTreeSearch(self.game)
        
        self.game.display_board()
        MCTSStart = time.time()
        agent.monteCarloSearch(rollouts)

        print("best move:")
        bestMove = agent.strongest_move()
        print(bestMove)
        self.game.turn(bestMove)

        agent.updateTree(bestMove)
        self.game.display_board()

        # print return if the puzzle was solved correctly or not
        if self.game.board == answer1 or self.game.board == answer2:
            print("CORRECT")
            return "CORRECT"
        else:
            print("INCORRECT")
            return "INCORRECT"
