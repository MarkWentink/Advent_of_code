
def read_input():

    with open('Data/AoC2019_3.txt') as f:
        wire1, wire2 = f.readlines()

    wire1 = wire1.strip().split(',')
    wire2 = wire2.strip().split(',')

    return wire1, wire2


def draw_path(wire):

    x, y = (0, 0)
    locations = [(0, 0)]

    for instruction in wire:
        if instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                y += 1
                locations.append((x, y))
        elif instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                x += 1
                locations.append((x, y))
        elif instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                y -= 1
                locations.append((x, y))
        elif instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                x -= 1
                locations.append((x, y))
        else:
            print("Error")
            break

    return locations




def star_one(wire1, wire2):

    locations1 = draw_path(wire1)
    locations2 = draw_path(wire2)

    temp = set(locations2)
    crossings = [value for value in locations1 if value in temp]  
    closest = sorted(list(map(sum, crossings)))[1]

    return closest



def star_two(wire1, wire2):

    locations1 = draw_path(wire1)
    locations2 = draw_path(wire2)
    temp = set(locations2)
    crossings = [value for value in locations1 if value in temp]  

    crossing_distance = list(map(lambda x : locations1.index(x) + locations2.index(x), crossings))
    shortest = sorted(crossing_distance)[1:2][0]

    return shortest
        


def Day_3():
    print("\n Day 3 solutions: \n")
    wire1, wire2 = read_input()
    print("Star one: ", star_one(wire1, wire2))
    print("Star two: ", star_two(wire1, wire2))
    print('\n------------------')

    return


if __name__ == '__main__':

    Day_3()
   