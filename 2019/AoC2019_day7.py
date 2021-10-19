import copy
import itertools

class Intcode_software:
    
    def __init__(self, code, inputs = []):
        
        self.pointer = 0
        self.memory = copy.deepcopy(code)
        self.pause = False
        self.halt = False
        self.outputs = []
        self.inputs = inputs
        
        self.opcodes = {
            '01' : self.opcode_01,
            '02' : self.opcode_02,
            '03' : self.opcode_03,
            '04' : self.opcode_04,
            '05' : self.opcode_05,
            '06' : self.opcode_06,
            '07' : self.opcode_07,
            '08' : self.opcode_08,
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
        # return immediate value or pointer to value
        
        if mode == '0':
            return self.memory[self.pointer + offset]
        else:
            return self.pointer + offset
    
    
    def opcode_01(self):
        
        modes = self.read_modes(3)

        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        p3 = self.parameter_loc(3)        
        
        self.memory[p3] = self.memory[p1] + self.memory[p2]
        self.pointer += 4
    

    def opcode_02(self):
        
        modes = self.read_modes(3)
        p1 = self.parameter_loc(1, modes[0])
        p2 = self.parameter_loc(2, modes[1])
        p3 = self.parameter_loc(3)        
        
        self.memory[p3] = self.memory[p1] * self.memory[p2]
        self.pointer += 4   
        
    def opcode_03(self):
             
        p1 = self.parameter_loc(1)
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
    
    def opcode_99(self):
        
        self.halt = True
        
        return



             
def read_input():
    with open('Data/AoC2019_7.txt') as file:
        ampcode = list(file.readlines()[0].split(','))
        ampcode = list(map(int, ampcode))

    return ampcode


def star_one(ampcode):
    phases = list(itertools.permutations([0,1,2,3,4]))
    results = []

    for phase in phases:
        signal = 0
        for x in range(5):
            amp = Intcode_software(ampcode, [phase[x], signal])
            amp.run()                    
            signal = amp.outputs[-1]
        results.append(signal)
    
    return max(results)
    

def star_two(ampcode):
    phase_settings = list(itertools.permutations([5,6,7,8,9]))
    results = []
    
    for phase_setting in phase_settings:
        signal = 0
        current_amp = 0
        amps = [Intcode_software(copy.deepcopy(ampcode), [phase_setting[x]]) for x in range(5)]
        
        while any([not x.halt for x in amps]):
            amps[current_amp].add_input(signal)
            amps[current_amp].run()
            signal = amps[current_amp].outputs[-1]
            
            if current_amp < 4:
                current_amp += 1
            else:
                current_amp = 0
        
        results.append(signal)
    return max(results)


def Day_7():
    print("\n Day 7 solutions: \n")
    ampcode = read_input()
    print("Star one: ", star_one(ampcode))
    print("Star two: ", star_two(ampcode))
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_7()
   