with open('input.txt', 'r') as fobj:
    ins = fobj.read().split('\n')
#
ins[0]
"""
Task: find infinite loops
I need a way to encode the value of the accumulator, what line we're on, and what lines we've been on so I can detect when a loop is about to start.
I want to output the value of the counter just _before_ the loop starts. so I should check the next line before I change the counter. I think a class is a good choice...

I somehow need to consider the entire sequence of instructions at once.
"""

class Machine:
    def __init__(self, instructions):
        self.accumulator = 0
        self.index = 0
        self.ins_done = []
        self.instructions = instructions
    
    def do_next(self):
        if self.index in self.ins_done:
            return self.accumulator
        if self.index == len(self.instructions):
            return self.accumulator
        self.ins_done.append(self.index)
        instruction = self.instructions[self.index]
        
        if instruction[:3] == 'acc':
            self.accumulator += int(instruction[4:])
            self.index += 1
            return False
        
        elif instruction[:3] == 'jmp':
            self.index += int(instruction[4:])
            return False
        
        elif instruction[:3] == 'nop':
            self.index += 1
            return False
        
        else:
            return False
#
machine = Machine(ins[:-1])
done = False
while not done:
    done = machine.do_next()
with open('output.txt','w') as fobj:
    fobj.write(str(done))
# part 2
# find the instruction that, when changed from jmp to nop or nop to jmp, makes it so that the sequence of instructions terminates by trying to carry out the instruction after the last instruction

def check_if_valid(instructions):
    done = False
    machine = Machine(instructions)
    done = False
    while not done:
        done = machine.do_next()
    if machine.index == len(instructions):
        return True, machine.accumulator
    else:
        return False, machine.accumulator

def find_the_right_one(instructions):
    for i, x in enumerate(instructions):
        if x[:3] == 'jmp':
            foo = instructions.copy()
            foo[i] = 'nop' + x[3:]
            valid, num = check_if_valid(foo)
            if valid:
                return num
        elif x[:3] == 'nop':
            foo = instructions.copy()
            foo[i] = 'jmp' + x[3:]
            valid, num = check_if_valid(foo)
            if valid:
                return num
num = find_the_right_one(ins[:-1])
with open('output2.txt','w') as fobj:
    fobj.write(str(num))