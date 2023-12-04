'''
Advent of Code 2023, Day 2:

We are given a list of games consisting of multiple draws of marbles from a bag.
e.g.: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

For part 1, the task is to verify whether a game is possible given an upper limit for the amount of 
red, green and blue marbles. (Marbles are put back in the bag after each draw).
Hence we need to check for each draw, that the nr of marbles drawn isn't bigger than the upper limit. 
The solution is the sum of game ids for allowed games.  

In part 2, we need to instead check what the upper limits for each game should have been to make them
valid games. The smallest possible upper limits are multiplied together to form the 'power' of a game.
The solution is the sum of all powers. 
'''


def day2():

    data = load_data()

    print("\nDAY 2")
    print("-------------\n")
    print(f"Solution for part 1: {part1(data)}")
    print(f"Solution for part 2: {part2(data)}")
    print('\n')

    return


def load_data():
    '''
    Loads in data from the given filepath, reading one line at a time, 
    stripping whitespace, and appending to a list. 
    '''
    data = []
    with open('./data/day2.txt') as f:
        for line in f.readlines():
            data.append(line.strip())

    return data




def part1(data):
    '''
    We first define a dictionary of allowed upper limits.
    Then, iterating through each game, we first split off the game id.
    Next, we split into individual draws and iterate over those.
    In each draw, we split into individual marble colours, and check whether the number is 
    bigger than our dictionary entries. 
    If it is, the game is a 'bad' game, and we list its game_id. 
    We could stop with the game immediately at this point, but currently the break only interrupts the inner for loop.
    Now that we have a list of bad game ids (with duplicates), we can subtract that list from a list of all game_ids, and sum the result.



    ''' 
    allowed = {'red' : 12,
          'blue' : 14,
          'green' : 13}
    
    bad_games = []

    for game in data:

        game_id = int(game.split(':')[0].split(' ')[1])
        
        for draw in game.split(':')[1].split(';'):

            for i in range(len(draw.split(','))):
                nr_marbles = int(draw.split(',')[i].strip().split(' ')[0])
                colour = draw.split(',')[i].strip().split(' ')[1]
                
                if nr_marbles > allowed[colour]:
                    bad_games.append(game_id)
                    break

    sum(range(1, len(data)+1))-sum(list(set(bad_games)))

    return sum(range(1, len(data)+1))-sum(list(set(bad_games)))


def part2(data):
    '''
    We follow the same process to identify nr of marbles and colours.
    Instead of comparing them against some upper limit, we simply keep track 
    of the biggest value that comes up using a dictionary.
    After each game, we multiply the dictionary entries for the three colours, add to a running total,
    and reset the dictionary. 
    '''
    counts = 0
    for game in data:
        biggest = {'red':0,
                'blue':0,
                'green':0}
        
        for draw in game.split(':')[1].split(';'):

            for i in range(len(draw.split(','))):

                nr_marbles = int(draw.split(',')[i].strip().split(' ')[0])
                colour = draw.split(',')[i].strip().split(' ')[1]

                if nr_marbles > biggest[colour]:
                    biggest[colour] = nr_marbles
                    
        product = 1
        for cube in list(biggest.values()):
            product *= cube
        
        counts += product
    
    return counts



if __name__ == '__main__':
    day2()