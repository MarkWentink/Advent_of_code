import copy


"""
Note: compared to previous versions of Intcode, opcodes 3 and 4 have been edited. 
To receive input, Opcode 3 now calls a new function 'check square', which looks up the robots current position on a map and returns
the color of the current tile. If the robot has never been on this tile before, it adds the coordinates to the map and returns 'black'.

If there are outputs in the output list (always the case except for the first step), opcode 3 also calls the 'paint and move' function, 
which edits the map with the new color of the tile, and updates the robot's location and direction. It then clears the output list 
awaiting new outputs.

For star two, a 'draw_ID' function has been created to print to screen the black and white entries in the map. 

""" 

class Intcode_software:
    
    def __init__(self, code, inputs = []):
        
        self.pointer = 0
        self.memory = copy.deepcopy(code)
        self.pause = False
        self.halt = False
        self.outputs = []
        self.inputs = inputs
        self.relative_base = 0
        self.direction = 0
        self.location = (0, 0)
        self.map = {}
        
        self.opcodes = {
            '01' : self.opcode_01,
            '02' : self.opcode_02,
            '03' : self.opcode_03,
            '04' : self.opcode_04,
            '05' : self.opcode_05,
            '06' : self.opcode_06,
            '07' : self.opcode_07,
            '08' : self.opcode_08,
            '09' : self.opcode_09,
            '99' : self.opcode_99,
        }
        
        return

    
    def run(self):
        
        while not (self.halt or self.pause):
  
            opcode = self.read_instruction()
            self.opcodes[opcode]()
    
            

    
    def read_instruction(self):
        
        opcode = self.memory[self.pointer]
        opcode = str(opcode).zfill(5)[-2:]
        return opcode
    
    def read_modes(self, nr_arg):
        modes = []
        modes = str(self.memory[self.pointer]).zfill(nr_arg+2)[:-2][::-1]
        return modes
            
    
    def parameter_loc(self, offset = 0, mode = '0'):
        # return immediate value or pointed to value
        if mode == '0':
            loc =  int(self.memory[self.pointer + offset])
        elif mode == '2':
            loc =  int(self.relative_base + self.memory[self.pointer + offset])
        else:
            loc =  int(self.pointer + offset)
            
        while loc >= len(self.memory):
            self.memory.append(0)
                    
        return loc
    
    
    def opcode_01(self):
        
        #print("welcome to opcode 1")
        modes = self.read_modes(3)
        #print("modes:", modes)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        p3 = self.parameter_loc(3, modes[2])        
        
        #print("Parameter locations: ", p1, p2, p3)
        self.memory[p3] = self.memory[p1] + self.memory[p2]
        self.pointer += 4
    
    def opcode_02(self):
        
        modes = self.read_modes(3)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        p3 = self.parameter_loc(3, modes[2])        
        
        self.memory[p3] = self.memory[p1] * self.memory[p2]
        self.pointer += 4   
    
    
    def opcode_03(self):
        
        if len(self.outputs) != 0:
            self.paint_and_move()

        modes = self.read_modes(1)
        p1 = self.parameter_loc(1, modes[0])
        val = self.check_square()
        
        if val != None:
            self.memory[p1] = val
            self.pointer += 2
        else:
            self.pause = True  
        
        return
    

    
    def paint_and_move(self):
        
        self.map[self.location] = self.outputs.pop(0)
        turn = self.outputs.pop(0)
        
        if turn == 0:
            self.direction = (self.direction - 90) % 360
        else:
            self.direction = (self.direction + 90) % 360
        
        
        if self.direction == 0:
            self.location = (self.location[0], self.location[1]+1)
        elif self.direction == 90:
            self.location = (self.location[0]+1, self.location[1])
        elif self.direction == 180:
            self.location = (self.location[0], self.location[1]-1)
        else:
            self.location = (self.location[0]-1, self.location[1])
            
        self.outputs.clear()
        
        
        
    
    def check_square(self):
        
        if self.location not in self.map.keys():
            self.map[self.location] = 0
            
        return self.map[self.location]
        
    
    def add_input(self, value):
        
        self.inputs.append(value)
        
        if self.pause:
            self.pause = False
        
        
        return

    
    def opcode_04_print(self):
        
        modes = self.read_modes(1)
        p1 = self.parameter_loc(1, modes[0])
        #print("location ",p1)
        print(self.memory[p1])
        
        self.pointer += 2
        
        return
    
    
    def opcode_04(self):
        
        modes = self.read_modes(1)
        p1 = self.parameter_loc(1, modes[0])
        self.outputs.append(self.memory[p1])
        
        self.pointer += 2
        
        return
    
    def opcode_05(self):
        
        modes = self.read_modes(2)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        
        if int(self.memory[p1]) != 0:
            self.pointer = int(self.memory[p2])
        else:
            self.pointer += 3
        
        return
    
    def opcode_06(self):
        
        modes = self.read_modes(2)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        
        if int(self.memory[p1]) == 0:
            self.pointer = int(self.memory[p2])
        else:
            self.pointer += 3        
        
        return
    
    def opcode_07(self):
        
        modes = self.read_modes(3)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        p3 = self.parameter_loc(3, modes[2])
        
        if self.memory[p1] < self.memory[p2]:
            self.memory[p3] = 1
        else:
            self.memory[p3] = 0
        
        self.pointer += 4
        
        return
    
    def opcode_08(self):
        
        modes = self.read_modes(3)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        p3 = self.parameter_loc(3, modes[2])
        
        if self.memory[p1] == self.memory[p2]:
            self.memory[p3] = 1
        else:
            self.memory[p3] = 0
        
        self.pointer += 4
        
        return
    
    def opcode_09(self):
        
        modes = self.read_modes(1)
        p1 = self.parameter_loc(1, modes[0])
        
        self.relative_base += self.memory[p1]
        
        self.pointer += 2
    
    def opcode_99(self):
        
        self.halt = True
        
        return
    
        
        
def get_input():

    with open('Data/AoC2019_11.txt') as f:
        for line in f.readlines():
            data = line.strip().split(',')
            data = list(map(int, data))
    
    return data


def star_one():
    
    data = get_input()
    painter = Intcode_software(data)
    # starting tile is black
    painter.map[(0, 0)] = 0
    painter.run()
    
    return len(painter.map)


def star_two():
    
    data = get_input()
    painter = Intcode_software(data)
    # starting tile is white
    painter.map[(0, 0)] = 1
    painter.run()
    
    x_min = min(list(map(lambda x: x[0], painter.map.keys())))
    x_max = max(list(map(lambda x: x[0], painter.map.keys())))
    y_min = min(list(map(lambda x: x[1], painter.map.keys())))
    y_max = max(list(map(lambda x: x[1], painter.map.keys())))

    hull = []
    for i in range(y_max, y_min-1, -1):
        row = ''
        for j in range(x_min, x_max+1):
            if (j, i) in painter.map.keys():
                if painter.map[(j, i)] == 1:
                    row += '1'
                else:
                    row +=' '

            else:
                row += ' '
        print(row)
        
    return


def Day_11():
    print("\n Day 10 solutions: \n")
    print("Star one: ", star_one())
    print("Star two: ")
    star_two()
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_11()    