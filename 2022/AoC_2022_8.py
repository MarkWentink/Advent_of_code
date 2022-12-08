import numpy as np

def day_8():

    data = load_data()
    print(data)
    print(data.shape)
    visible = np.zeros((99,99), dtype=int)
    #print(visible)
    # Part 1
    
    for k in range(4):
        for i in range(data.shape[0]):
            visible[i][0] = 1
            for j in range(data.shape[1]):
                if all([data[i][x] < data[i][j] for x in range(j)]):
                    visible[i][j] = 1
                
        data = np.rot90(data)
        visible = np.rot90(visible)
        #print(data)

    #print(visible)
    
    print(f"Solution to part 1: {np.sum(visible)}")


    # Part 2

    # scenic score
    scenery = np.zeros((99,99), dtype=int)
    for i in range(scenery.shape[0]):
        for j in range(scenery.shape[1]):
            scenery[i][j] = scenic(data, (i, j))
    

    print(scenery)
    
    print(f"Solution to part 2: {np.amax(scenery}")
 
    return



def scenic(dat, tree):
    # look left

    distances = []
    i, j = tree
    for r in range(4):
        
        k = j+1
        distance = 0
        while (k < dat.shape[1]):
            if (dat[i][k] < dat[i][j]):
                distance += 1
                k += 1
            else:
                distance += 1
                break
        distances.append(distance)
        dat = np.rot90(dat)
        i, j = dat.shape[0]-j-1, i
    #print(distances)
    return np.prod(distances)




def load_data():
    data = []
    with open('./data/day8.txt') as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip()])
    return np.array(data)



if __name__ == '__main__':
    day_8()


