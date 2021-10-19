


def read_input():

    modules = []

    with open('Data/AoC2019_1.txt') as file:
        for line in file.readlines():
            modules.append(int(line.strip()))

    return modules


def calculate_fuel(weight):
    fuel = 0
    while weight//3 - 2 > 0:
        fuel += weight//3 - 2
        weight = weight//3 - 2
    return fuel

def star_one(data):

    module_fuel = sum(list(map(lambda x: x//3 - 2, data)))

    return module_fuel

def star_two(data):

    total = sum(list(map(calculate_fuel, data)))

    return total

def Day_1():
    print("Day 1 solutions: \n")
    data = read_input()
    print("Star one: ", star_one(data))
    print("Star two: ", star_two(data))
    print('\n------------------')

    return


if __name__ == '__main__':

    Day_1()
