def day_7():

    data = load_data()

    paths = ['//']
    pwd = ''
    unique_folders = []

    for instruction in data:
        #print(instruction)

        if instruction[:4] == '$ cd':
            if instruction == '$ cd ..':
                pwd = pwd.rsplit('/', 2)[0]
                pwd += '/'
                #print(pwd)
            else:
                pwd = pwd + instruction[5:] + '/'
                #print(pwd)

        elif instruction[:4] == '$ ls':
            pass
        
        elif instruction[:3] == 'dir':
            paths.append(pwd + instruction[4:] + '/')
            unique_folders.append(pwd + instruction[4:] + '/')
        else:
            paths.append(pwd + instruction.split()[1] + ':' + instruction.split()[0])


    # Part 1

    structure = {}
    for folder in unique_folders:
        structure[folder] = sum([int(x.split(':')[1]) for x in paths if (x[:len(folder)] == folder) and(':' in x)])

    small = [x for x in structure.keys() if structure[x]<=100000]

    print(f"Solution to part 1: {sum([structure[x] for x in small])}")


    # Part 2

    # calculate total size
    total_size = sum([int(x.split(':')[1]) for x in paths if ':' in x])
    #print("Total size: ", total_size)
    to_delete = total_size - 40000000
    #print(to_delete)

    big_enough = [x for x in structure.keys() if structure[x]>= to_delete]
    big_enough = [(x, structure[x]) for x in big_enough]
    smallest = [x[1] for x in big_enough if x[1] == min([x[1] for x in big_enough])]

    
    print(f"Solution to part 2: {smallest[0]}")
 
    return








def load_data():
    data = []
    with open('./data/day7.txt') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data



if __name__ == '__main__':
    day_7()


