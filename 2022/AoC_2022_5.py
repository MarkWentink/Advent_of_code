def day_5():

    data = load_data()
    #print(data)

    i = 0
    chart = []
    while data[i] != '':
        chart.append(data[i])
        i += 1
    
    instructions = data[i+1:]

    #print(instructions)


    print(f"Solution to part 1: ")
    
    #manual
    chart = [['G, D, V, Z, J, S, B'],
    ['Z, S, M, G, V, P'],
    ['C, L, B, S, W, T, Q, F'],
    ['H, J, G, W, M, R, V, Q'],
    ['C, L, S, N, F, M, D'],
    ['R, G, C, D'],
    ['H, G, T, R, J, D, S, Q'],
    ['P, F, V'],
    ['D, R, S, T, J']]

    chart = [x[0].split(', ') for x in chart]

    #print(chart)
    '''
    for instruction in instructions:
        nr = int(instruction.split(' from')[0].split('move ')[1])
        start = int(instruction.split('from ')[1].split(' to')[0])
        end = int(instruction.split('to ')[1])

        for i in range(nr):
            chart[end-1].append(chart[start-1].pop())
           
        
    print(chart)
    # Part 1
    '''

    # Part 2


    for instruction in instructions:
        nr = int(instruction.split(' from')[0].split('move ')[1])
        start = int(instruction.split('from ')[1].split(' to')[0])
        end = int(instruction.split('to ')[1])

        chunk = list(reversed(chart[start-1]))[:nr]
        chart[start-1] = chart[start-1][:-nr]
        chart[end-1] = chart[end-1]+list(reversed(chunk))

    print(chart)
           
        
    
    print(f"Solution to part 2: ")
 
    return








def load_data():
    data = []
    with open('./data/day5.txt') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data



if __name__ == '__main__':
    day_5()


