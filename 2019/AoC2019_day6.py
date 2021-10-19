
def read_input():

    moons = []
    orbits = {}

    # we want to retain a list of all the bodies in the problem (moons)
    # as well as map which bodies orbit which (orbits)
    with open('Data/AoC2019_6.txt') as f:
        for line in f.readlines():
            #moons.append(line.strip().split(')')[1])
            if line.split(')')[0] in orbits.keys():
                orbits[line.split(')')[0]].append(line.strip().split(')')[1])
            else:    
                orbits[line.strip().split(')')[0]] = [line.strip().split(')')[1]]

    return orbits

def star_one(orbits):

    # Initialise galaxy, with COM at distance 0
    galaxy = [('COM', 0)]
    i = 0
    total_orbits = 0

    while i < len(galaxy):
        # try to retrieve the bodies in orbit around the current moon
        try:
            # insert those bodies after the current moon along with the distance from COM
            for moon in orbits[galaxy[i][0]]:
                galaxy.insert(i+1, (moon, galaxy[i][1]+1))
                # add their distance from COM to the total number of orbits.
                total_orbits += galaxy[i][1]+1
                
            i += 1
        # if there are none, move down the list
        except:
            i += 1

    return total_orbits


def trace_lineage(moon, orbits):

    position = moon
    lineage = [moon]
    while position != 'COM':
        position = list(x for x in orbits.keys() if position in orbits[x])[0]
        lineage.append(position)
    
    return lineage


def star_two(orbits):

    lineage_you = trace_lineage('YOU', orbits)
    lineage_santa = trace_lineage('SAN', orbits)

    while lineage_you[-2] == lineage_santa[-2]:
        lineage_you = lineage_you[:-1]
        lineage_santa = lineage_santa[:-1]

    distance = len(lineage_you)-2 + len(lineage_santa)-2
    
    return distance


def Day_6():
    print("\n Day 6 solutions: \n")
    orbits = read_input()
    print("Star one: ", star_one(orbits))
    print("Star two: ", star_two(orbits))
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_6()
   