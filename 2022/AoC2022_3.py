def day_3():

    data = load_data()
    total = 0
    for rucksack in data:
        double = list(set(rucksack[:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2:])))[0]
        if ord(double) in range(65,91):
            score = ord(double)-38
        else:
            score = ord(double)-96
        
        total += score
    print(f"Solution to part 1: {total}")
        

    
    # Part 1
    packs = []
    for i in range(len(data)//3):
        packs.append(data[3*i:3*i+3])

    total = 0
    for pack in packs:
        double = list(set(pack[0]).intersection(pack[1]).intersection(pack[2]))[0]
        if ord(double) in range(65,91):
            score = ord(double)-38
        else:
            score = ord(double)-96
        
        total += score

    # Part 2

    print(f"Solution to part 2: {total}")
 
    return





def load_data():
    data = []
    with open('./data/day3.txt') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data



if __name__ == '__main__':
    day_3()


