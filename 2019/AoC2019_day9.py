import copy

class Intcode_software:
    
    def __init__(self, code, inputs = []):
        
        self.pointer = 0
        self.memory = copy.deepcopy(code)
        self.pause = False
        self.halt = False
        self.outputs = []
        self.inputs = inputs
        self.relative_base = 0
        
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
            #print("Current pointer: ", self.pointer)
            #print(self.memory, '\n\n')
            
            #print("relative base: ", self.relative_base)
            opcode = self.read_instruction()
            #print(opcode)
            self.opcodes[opcode]()
    
            

    
    def read_instruction(self):
        
        
        opcode = self.memory[self.pointer]
        #print("opcode is: ", str(opcode).zfill(5))
        opcode = str(opcode).zfill(5)[-2:]
        return opcode
    
    def read_modes(self, nr_arg):
        modes = []
        modes = str(self.memory[self.pointer]).zfill(nr_arg+2)[:-2][::-1]
        #print("modes ", modes)
        return modes
            
    
    def parameter_loc(self, offset = 0, mode = '0'):
        # return immediate value or pointed to value
        if mode == '0':
            loc =  self.memory[self.pointer + offset]
        elif mode == '2':
            loc =  self.relative_base + self.memory[self.pointer + offset]
        else:
            loc =  self.pointer + offset
            
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
        
        modes = self.read_modes(1)
        p1 = self.parameter_loc(1, modes[0])
        val = self.read_input()
        
        if val != None:
            self.memory[p1] = val
            self.pointer += 2
        else:
            self.pause = True
        
        return
    
    def read_input(self):
        
        if len(self.inputs) > 0:
            return int(self.inputs.pop(0))
        else:
            return None
        
    
    def add_input(self, value):
        
        self.inputs.append(value)
        
        if self.pause:
            self.pause = False
        
        
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
            self.pointer = self.memory[p2]
        else:
            self.pointer += 3
        
        return
    
    def opcode_06(self):
        
        modes = self.read_modes(2)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        
        if int(self.memory[p1]) == 0:
            self.pointer = self.memory[p2]
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

  
def read_input():
    with open('Data/AoC2019_9.txt') as file:
        boost = list(file.readlines()[0].split(','))
        boost = list(map(int, boost))

    return boost


def star(code, input):

    booster = Intcode_software(copy.deepcopy(code),[input])
    booster.run()

    return booster.outputs



def Day_9():
    print("\n Day 9 solutions: \n")
    boost = read_input()
    print("Star one: ", star(boost, 1))
    print("Star two: ", star(boost, 2)) 
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_9()