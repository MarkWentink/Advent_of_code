#Input is a .txt file where each line contains 2 letters, the first ranging A-C, the second X-Z, space-separated. 

def day_2():

    data = load_data()
    
    # Part 1 : Interpret ABC as opponent moves and XYZ as your moves.
    # Calculate total score based on move and outcome.

    # For each game in the list, feed into the count_score function, and sum all the results. 
    print(f"Solution to part 1: {sum([count_score(x) for x in data])}")


    # Part 2 : 
    # Calculate total score based on move and outcome. 
    # In this case, X, Y, Z does not represent the player move, but the outcome of the game. (The player move has to be deduced)
    print(f"Solution to part 2: {sum([count_score_2(x) for x in data])}")
 
    return

def count_score(game):
    """
    Calculates the total score of a RPS game. 
    Score is calculated in two parts: 
    - the player is awarded 1, 2, or 3 points based on whether they played Rock, Paper or Scissors (given by X, Y, Z)
    - the player is awarded 0, 3, or 6 points based on whether they lost, drew, or won the game. (must be deduced)
    
    input: two letters as a tuple:
    - A, B, C represents the opponent's move, rock, paper, scissors
    - X, Y, Z represents the player move. 

    output: total score as an int.
    """
    score = 0

    # player move
    if game[1] == 'X':
        score += 1
    elif game[1] == 'Y':
        score += 2
    else:
        score += 3
    
    # game outcome, mapped as a dictionary based on the rock paper scissors rules 
    outcome = {
        'AX':3,
        'AY':6,
        'AZ':0,
        'BX':0,
        'BY':3,
        'BZ':6,
        'CX':6,
        'CY':0,
        'CZ':3
    }
    score += outcome[game[0]+game[1]]
    return score


def count_score_2(game):
    """
    Calculates the total score of a RPS game. 
    Score is calculated in two parts: 
    - the player is awarded 1, 2, or 3 points based on whether they played Rock, Paper or Scissors (this must be deduced)
    - the player is awarded 0, 3, or 6 points based on whether they lost, drew, or won the game. (this is given by X, Y, Z)
    
    input: two letters as a tuple:
    - A, B, C represents the opponent's move, rock, paper, scissors
    - X, Y, Z represents the outcome of the game.  

    output: total score as an int.
    """
    # Game outcome
    score = 0
    if game[1] == 'X':
        score += 0
    elif game[1] == 'Y':
        score += 3
    else:
        score += 6

    # Player move
    move = {
        'AX':3, # opponent Rock, outcome loss ==> player Scissors, worth 3 points. 
        'AY':1,
        'AZ':2,
        'BX':1,
        'BY':2,
        'BZ':3,
        'CX':2,
        'CY':3,
        'CZ':1
    }
    score += move[game[0]+game[1]]
    return score



def load_data():
    """
    load_data() parses a .txt file, extracting the Rock Paper Scissors moves and separating them out into a list of lists. 

    input: Each line contains two space-separated letters

    output: list of lists containing the RPS moves. 
    """
    data = []
    with open('./data/day2.txt') as f:
        for line in f.readlines():
            data.append(line.strip().split())
    return data



if __name__ == '__main__':
    day_2()


