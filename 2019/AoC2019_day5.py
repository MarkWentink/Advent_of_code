import copy

class Intcode:
    def __init__(self, code, input):
        self.code = code
        self.pointer = 0
        self.operation = str(self.code[self.pointer])
        self.input = [input]
        self.output = []

        
    def run(self):

        while self.operation[-1] != '9':
            #print("\n",'pointer: ', self.pointer, " operation: ",self.operation)
            
            if self.operation[-1] in ['1', '2', '7', '8']:
                
                # opcodes 1 and 2 each take 3 parameters, the third parameter is always in position mode
                # If the opcode is shorter than 3 digits, all parameters are positions. 
                if len(self.operation) < 3:
                    p1 = int(self.code[int(self.code[self.pointer+1])])
                    p2 = int(self.code[int(self.code[self.pointer+2])])
                
                # if there are 3 digits, only the mode of p1 is specified, p2 is a position
                elif len(self.operation) == 3:
                    
                    if self.operation[0] == '1':
                        p1 = int(self.code[self.pointer+1])
                    elif self.operation[0] == '0':
                        p1 = int(self.code[int(self.code[self.pointer+1])])
                    else: 
                        print("Error p1")
                    
                    p2 = int(self.code[int(self.code[self.pointer+2])])
                
                # if there are 4 digits, both p1 and p2 are specified. 
                elif len(self.operation) == 4:
                    if self.operation[1] == '1':
                        p1 = int(self.code[self.pointer+1])
                    elif self.operation[1] == '0':
                        p1 = int(self.code[int(self.code[self.pointer+1])])
                    else: 
                        print("Error p1")
                        
                    if self.operation[0] == '1':
                        p2 = int(self.code[self.pointer+2])
                    elif self.operation[0] == '0':
                        p2 = int(self.code[int(self.code[self.pointer+2])])
                    else: 
                        print("Error p2")
                else:
                    print("Error interpreting instruction")
                    return
             
                #p3 is always in position mode    
                p3 = int(self.code[self.pointer+3])

                # Send parameters to appropriate opcode
                if self.operation[-1] == '1':
                    self.opcode01(p1, p2, p3)
                elif self.operation[-1] == '2':
                    self.opcode02(p1, p2, p3)
                elif self.operation[-1] == '7':
                    self.opcode07(p1, p2, p3)
                elif self.operation[-1] == '8':
                    self.opcode08(p1, p2, p3)
                else:
                    print("Error")
                    return
                #Increment pointer
                self.pointer += 4

                
            elif self.operation[-1] == '3':
                self.opcode03()
            elif self.operation[-1] == '4':
                self.opcode04()
            elif self.operation[-1] in ['5', '6']:
                
                if len(self.operation) < 3:
                    p1 = self.code[self.code[self.pointer+1]]
                    p2 = self.code[self.code[self.pointer+2]]
                else:
                    if self.operation[-3] == '0':
                        p1 = self.code[self.code[self.pointer+1]]
                    elif self.operation[-3] == '1':
                        p1 = self.code[self.pointer+1]
                    
                    if len(self.operation) == 4:
                        p2 = self.code[self.pointer+2]
                    else:
                        p2 = self.code[self.code[self.pointer+2]]
                
                if self.operation[-1] == '5':
                    self.opcode05(p1, p2)
                elif self.operation[-1] == '6':
                    self.opcode06(p1, p2)
                else:
                    print("Error")
                    return
                
            else:
                print("Error")
                return
            self.operation = str(self.code[self.pointer])

        
        
        
    def initialise(self, count):
        self.code[1] = count // 100
        self.code[2] = count % 100
        
    def reset(self):
        self.code = copy.deepcopy(backup)
        self.pointer = 0
        
    def opcode01(self, p1, p2, p3):
        
        self.code[p3] = p1 + p2
        
       # print(self.code[0:82])
      #  print('position 224 ', self.code[224], 'position 225 ', self.code[225])
       # print('position 69 ', self.code[69], 'position 118 ', self.code[118])

        
    def opcode02(self, p1, p2, p3):
   
        self.code[p3] = p1 * p2
    
        #print(self.code[0:82])
       # print('position 224 ', self.code[224], 'position 225 ', self.code[225])
        #print('position 69 ', self.code[69], 'position 118 ', self.code[118])

        
    def opcode03(self):

        self.code[self.code[self.pointer+1]] = self.input.pop()
        
        self.pointer += 2
        
    def opcode04(self):
                
        if len(self.operation) < 3:
            self.output.append(self.code[self.code[self.pointer+1]])
        else:
            self.output.append(self.code[self.pointer+1])
        
        self.pointer += 2
        
    def opcode05(self, p1, p2):
        
        if p1 != 0:
            self.pointer = p2
        else:
            self.pointer += 3
    
    def opcode06(self, p1, p2):
        
        if p1 == 0:
            self.pointer = p2
        else:
            self.pointer += 3
    
    def opcode07(self, p1, p2, p3):
        
        if p1 < p2:
            self.code[p3] = 1
        else:
            self.code[p3] = 0
            
            
    def opcode08(self, p1, p2, p3):
        
        if p1 == p2:
            self.code[p3] = 1
        else:
            self.code[p3] = 0
            




def read_input():

    with open('Data/AoC2019_5.txt') as file:
        intcode = list(file.readlines()[0].split(','))
        intcode = list(map(int, intcode))

    return intcode




def star(intcode, input):

    
    program = Intcode(copy.deepcopy(intcode), input)
    program.run()
    output = program.output[0]

    return output



def Day_5():
    print("\n Day 5 solutions: \n")
    intcode = read_input()
    print("Star one: ", star(intcode, '1'))
    print("Star two: ", star(intcode, '5'))
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_5()
   