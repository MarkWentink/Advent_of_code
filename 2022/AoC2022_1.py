def day_1():

    data = load_data()
    calorie_list = list(reversed(sorted([sum(x) for x in data])))
    
    # Part 1
    print(f"Solution to part 1: {calorie_list[0]}")

    # Part 2
    print(f"Solution to part 2: {sum(calorie_list[0:3])}")
 
    return


def load_data():
    data = []
    with open('./data/day1.txt') as f:
        elf = []
        for line in f.readlines():
            if line.strip() != '':
                elf.append(int(line.strip()))
            else:
                data.append(elf)
                elf = []
    return data



if __name__ == '__main__':
    day_1()


