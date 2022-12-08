def day_2():

    data = load_data()
    #print(data)

    
    # Part 1
    print(sum([count_score(x) for x in data]))
    print(f"Solution to part 1: ")


    # Part 2
    print(sum([count_score_2(x) for x in data]))

    print(f"Solution to part 2: ")
 
    return

def count_score_2(game):

    score = 0
    if game[1] == 'X':
        score += 0
    elif game[1] == 'Y':
        score += 3
    else:
        score += 6

    move = {
        'AX':3,
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

def count_score(game):

    score = 0
    if game[1] == 'X':
        score += 1
    elif game[1] == 'Y':
        score += 2
    else:
        score += 3
    
    
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

def load_data():
    data = []
    with open('./data/day2.txt') as f:
        for line in f.readlines():
            data.append(line.strip().split())
    return data



if __name__ == '__main__':
    day_2()


