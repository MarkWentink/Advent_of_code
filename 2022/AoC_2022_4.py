def day_4():

    data = load_data()

    count = 0
    for pair in data:
        if check_overlap(pair) == True:
            count += 1    
    print(f"Solution to part 1: {count}")
    

    
    # Part 1


    # Part 2
    count = 0
    for pair in data:
        if check_part_overlap(pair) == True:
            count += 1 
    print(f"Solution to part 2: {count}")
 
    return

def check_overlap(pair):
    #print(pair)
    r1 = pair[0].split('-')
    r2 = pair[1].split('-')
    
    if (int(r1[0]) >= int(r2[0])) and (int(r1[1]) <= int(r2[1])):
        #print('Match')
        return True
    elif (int(r2[0]) >= int(r1[0])) and (int(r2[1]) <= int(r1[1])):
        #print('match')
        return True
    else:
        #print('no match')
        return False


def check_part_overlap(pair):
    r1 = pair[0].split('-')
    r2 = pair[1].split('-')
    
    l1 = set(range(int(r1[0]), int(r1[1])+1))
    l2 = set(range(int(r2[0]), int(r2[1])+1))

    if (len(l1-l2) != len(l1)) or (len(l2-l1) != len(l2)):
        return True
    else:
        return False



def load_data():
    data = []
    with open('./data/day4.txt') as f:
        for line in f.readlines():
            data.append(line.strip().split(','))
    return data



if __name__ == '__main__':
    day_4()


