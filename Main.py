import Tests

##############--------- MAIN PROGRAM CODE ------------##################


while True:
    
    while True:
        simulation = 0
        try:
            print("simulation options: ")
            print("1 = minimax vs minimax ")
            print("2 = monte carlo tree search vs minimax")
            print("3 = human vs minimax")
            print("4 = human vs monte carlo tree search ")
            print("5 = minimax puzzle ")
            print("6 = monte carlo puzzle")
            print(" ")
            simulation = int(input("Input simulation option: "))
        except ValueError:
            print("invalid type")
        if  1 <= simulation <=6: 
            break
        else:
            print("invalid option please try again")
            print(" ")
          
    

    test = Tests.Test()
    winnerCount = 0
    results = []
    rollouts = 0
    depth = 0
    h1 = 0
    h2 = 0
    #this value can be modified for bulk testing (this option is not given to the user)
    for i in range(0, 1):
        try:
            if simulation == 1 or simulation == 2 or simulation == 3 or simulation == 5:
                depth = int(input("enter depth"))
                h1 = int(input("input evaluation function to be used (1 to 3): "))
                if h1 < 1 or h1 > 3:
                    print("invalid input")
                    break      
                if depth <= 0:
                    print("invalid input")
                    break                        
            if simulation == 1:
                h2 = int(input("input second evaluation function to be used (1 to 3): "))
                if h1 < 1 or h1 > 3:
                    print("invalid input")
                    break      
            if simulation == 2 or simulation == 4 or simulation == 6:
                rollouts = int(input("enter the number of rollouts (typically in the range 500-6000) : "))
                if rollouts <= 1:
                    print("need higher rollout")
        except ValueError:
            print("invalid type")
            break

        
        if simulation == 1:
            loser, totalMoves, averageTime1, averageTime2 = test.minimax_VS_minimax(depth, h1, h2)
        if simulation == 2:
            loser,totalMoves,averageTime1,averageTime2 =test.MonteCarlo_VS_minimax(depth,h1,rollouts)
        if simulation == 3:
            loser,totalMoves,averageTime1,averageTime2 =test.human_vs_MINIMAX(h1,depth)
        if simulation == 4:
            loser,totalMoves,averageTime1,averageTime2 =test.human_vs_MCTS(rollouts)
        if simulation == 5:
            test.puzzle_minimax(depth,h1)
            break
        if simulation == 6:
            test.puzzle_MCTS(rollouts)
            break
        if loser == "X":
            winnerCount += 1
        results.append([loser, totalMoves, averageTime1, averageTime2])
        test.reset_game()
    print(winnerCount)
    print(results)



