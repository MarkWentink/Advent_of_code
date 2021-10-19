
import copy

def read_input():

    with open('Data/AoC2019_2.txt') as file:
        intcode = list(file.readlines()[0].split(','))
        intcode = list(map(int, intcode))

    return intcode


class Intcode:
    def __init__(self, code):
        self.code = code
        self.pointer = 0
        
    def run(self):
        while self.code[self.pointer] != 99:
            if self.code[self.pointer] == 1:
                self.opcode01()
            elif self.code[self.pointer] == 2:
                self.opcode02()
            else:
                print("Error")
        #print('Stop code encountered')
        
        
    def initialise(self, count):
        self.code[1] = count // 100
        self.code[2] = count % 100
        
    def reset(self, data):
        self.code = copy.deepcopy(data)
        self.pointer = 0
        
    def opcode01(self):
        self.code[self.code[self.pointer+3]] = self.code[self.code[self.pointer+1]] + self.code[self.code[self.pointer+2]]
        self.pointer += 4
        #print(self.code)
        
    def opcode02(self):
        self.code[self.code[self.pointer+3]] = self.code[self.code[self.pointer+1]] * self.code[self.code[self.pointer+2]]
        self.pointer += 4
        #print(self.code)
        

def star_one(data):

    program = Intcode(copy.deepcopy(data))
    program.initialise(1202)
    program.run()

    return program.code[0]

def star_two(data):
    
    
    program = Intcode(copy.deepcopy(data))

    count = 0
    while (program.code[0] != 19690720) & (count < 10000):
        count += 1
        program.reset(data)
        program.initialise(count)
        program.run()

    return count




def Day_2():
    print("\n Day 2 solutions: \n")
    intcode = read_input()
    print("Star one: ", star_one(intcode))
    print("Star two: ", star_two(intcode))
    print('\n------------------')

    return


if __name__ == '__main__':

    Day_2()
   