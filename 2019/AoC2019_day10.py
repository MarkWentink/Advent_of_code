import math

def get_asteroid_coordinates(galaxy):
    asteroid_coordinates = []

    for x in range(len(galaxy)):
        for y in range(len(galaxy[x])):
            if galaxy[x][y] == '#':
                asteroid_coordinates.append((y,x))
    
    return asteroid_coordinates

    

def check_LoS(current_LoS, current, asteroid):
    
    
    steps = math.gcd(asteroid[0]-current[0], asteroid[1]-current[1])
    for i in range(1, steps):
        step_size = tuple(((asteroid[0]-current[0]) // steps , (asteroid[1]-current[1]) // steps ))
        if tuple((current[0]+i*step_size[0], current[1]+i*step_size[1])) in current_LoS:
            return False
    
    return True

def star_one():
    
    galaxy = get_day10()
    asteroid_coordinates = get_asteroid_coordinates(galaxy)
    
    visibility = {}
    for i in range(len(asteroid_coordinates)):

        current = asteroid_coordinates[i]
        current_LoS = asteroid_coordinates[:i] + asteroid_coordinates[i+1:]
        i = 0
        while i <  len(current_LoS):
            asteroid = current_LoS[i]
            if not check_LoS(current_LoS, current, asteroid):
                current_LoS.remove(asteroid)
            else:
                i += 1

        visibility[current] = len(current_LoS)
    for key in visibility.keys():
        if visibility[key] == max(visibility.values()):
            return(key, visibility[key])
     
    return


def getAngle(a, b, c):
    
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    
    return ang + 360 if ang < 0 else ang



def star_two():
    galaxy = get_day10()
    station = star_one()[0]
    north = (station[0], 0)

    asteroid_coordinates = get_asteroid_coordinates(galaxy)
    asteroid_coordinates.remove(station)

    asteroids_angles = []

    for asteroid in asteroid_coordinates:
        asteroids_angles.append([asteroid, getAngle(north, station, asteroid)])

    unique_angles = sorted(set(map(lambda x: x[1], asteroids_angles)))
    for angle in unique_angles:
        conflicts = list(x for x in asteroids_angles if x[1] == angle)

        for conflict in conflicts:
            conflict[1] += 1000*sorted(conflicts, key = lambda x: abs(x[0][0]-station[0]) + abs(x[0][1]-station[1])).index(conflict)

    asteroid_200 = sorted(asteroids_angles, key = lambda x: x[1])[199]

    return asteroid_200[0]

def get_day10():

    with open('Data/AoC2019_10.txt') as f:
        galaxy = []
        for line in f.readlines():
            galaxy.append(line.strip())
            
    return galaxy

def Day_10():
    print("\n Day 10 solutions: \n")
    print("Star one: ", star_one()[1])
    print("Star two: ", star_two())
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_10()