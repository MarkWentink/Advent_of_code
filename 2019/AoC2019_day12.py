import copy

class Moon:
    
    def __init__(self, start_position):
        
        [self.x, self.y, self.z] = start_position
        [self.dx, self.dy, self.dz] = [0,0,0]
        
        return

import itertools
class Universe:
    
    
    def __init__(self, bodies):
        self.moons = bodies
        self.history = []
        self.repeat = False

        return
    
    def gravity(self):
        
        for pair in list(itertools.combinations(self.moons,2)):
            if pair[0].x < pair[1].x:
                pair[0].dx += 1
                pair[1].dx -= 1

            elif pair[0].x > pair[1].x:
                pair[0].dx -= 1
                pair[1].dx += 1
                
            if pair[0].y < pair[1].y:
                pair[0].dy += 1
                pair[1].dy -= 1

            elif pair[0].y > pair[1].y:
                pair[0].dy -= 1
                pair[1].dy += 1
                
            if pair[0].z < pair[1].z:
                pair[0].dz += 1
                pair[1].dz -= 1

            elif pair[0].z > pair[1].z:
                pair[0].dz -= 1
                pair[1].dz += 1
        return
                
    def velocity(self):
        
        for moon in self.moons:
            
            moon.x += moon.dx
            moon.y += moon.dy
            moon.z += moon.dz
        
        return
    
    def system_energy(self):
        
        energy = 0
        
        for moon in self.moons:
            energy += (abs(moon.x)+abs(moon.y)+abs(moon.z)) * (abs(moon.dx)+abs(moon.dy)+abs(moon.dz)) 
        
        return energy
    
    def save_state(self):
        
        state = []
        
        for moon in self.moons:
            state += [moon.x, moon.y, moon.z, moon.dx, moon.dy, moon.dz]
        
        if state not in self.history:
            self.history.append(tuple(state))
        else:
            print("History repeats itself")
            self.repeat = True
        
        return
    
    def solve_axis_x(self):
        
        stop = False
        steps = 0
        while not stop:
            
            self.gravity()
            self.velocity()
            steps += 1
            
            if all(x.dx == 0 for x in self.moons):
                return steps
            
    def solve_axis_y(self):
        
        stop = False
        steps = 0
        while not stop:
            
            self.gravity()
            self.velocity()
            steps += 1
            
            if all(x.dy == 0 for x in self.moons):
                return steps
            
    def solve_axis_z(self):
        
        stop = False
        steps = 0
        while not stop:
            
            self.gravity()
            self.velocity()
            steps += 1
            
            if all(x.dz == 0 for x in self.moons):
                return steps
            
            
    

def initialise_moons():
    
    start_positions = get_day12()
    moons = [Moon(start_positions[x]) for x in range(len(start_positions))]
    
    return moons


from math import gcd
def lcm(a, b):
    return abs(a*b) // gcd(a, b)


import re

def get_day12():
    positions = []
    with open('Data/AoC2019_12.txt') as f:
        for line in f.readlines():
            p = re.compile("(?=)[\d-]+")
            positions.append(list(map(int, p.findall(line))))
            
    return positions


def star_one():

    moons = initialise_moons()
    universe = Universe(moons)
    for i in range(1000):
        universe.gravity()
        universe.velocity()
    
    energy = universe.system_energy()

    return energy

def star_two():

    moons = initialise_moons()
    universe = Universe(moons)
    x = universe.solve_axis_x()

    moons = initialise_moons()
    universe = Universe(moons)
    y = universe.solve_axis_y()

    moons = initialise_moons()
    universe = Universe(moons)
    z = universe.solve_axis_z()

    period = lcm(lcm(x,y), z) * 2

    return period



def Day_12():
    print("\n Day 12 solutions: \n")
    print("Star one: ", star_one())
    print("Star two: ", star_two())
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_12()    
