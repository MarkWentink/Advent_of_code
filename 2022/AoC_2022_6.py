def day_6():

    data = load_data()
    data = data[0]
    print(data)


    

    # Part 1
    i = 0
    while len(set(data[i:i+4])) != 4:
        i += 1
    
    print(f"Solution to part 1: {i+4}")

    # Part 2

    i = 0
    while len(set(data[i:i+14])) != 14:
        i += 1    
        
    
    print(f"Solution to part 2: {i+14}")
 
    return








def load_data():
    data = []
    with open('./data/day6.txt') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data



if __name__ == '__main__':
    day_6()


