with open('input.txt','r') as fobj:
    lines = fobj.read().split('\n')[:-1]
import math
import numpy as np
class Ferry:
    def __init__(self, pos = [0, 0], angle = 0):
        self.pos = pos # position of the ferry [W/E, S/N]
        self.angle = angle # heading of the ferry in degrees. 0 = East, 90 = North
        
    def update(self, ins, use_numpy = False):
        """
        carry out the instruction ins
        """
        if ins[0] == 'N':
            self.pos[1] += int(ins[1:])
        elif ins[0] == 'S':
            self.pos[1] -= int(ins[1:])
        elif ins[0] == 'E':
            self.pos[0] += int(ins[1:])
        elif ins[0] == 'W':
            self.pos[0] -= int(ins[1:])
        elif ins[0] == 'F':
            dist = int(ins[1:])
            if use_numpy:
                c = np.cos(self.angle*np.pi/180)
                s = np.sin(self.angle*np.pi/180)
            else:
                c = math.cos(self.angle*math.pi/180)
                s = math.sin(self.angle*math.pi/180)
            self.pos[0] += c * dist
            self.pos[1] += s * dist
        elif ins[0] == 'L':
            self.angle += int(ins[1:])
        elif ins[0] == 'R':
            self.angle -= int(ins[1:])
        else:
            print('instruction ignored')
            pass
filip = Ferry()
for ins in lines:
    filip.update(ins, use_numpy = True)
ans = sum(map(abs, filip.pos))

# part 2
class Ferry:
    def __init__(self, pos = [0, 0], angle = 0, wp = [10, 1]):
        self.pos = pos # position of the ferry [W/E, S/N]
        self.angle = angle # heading of the ferry in degrees. 0 = East, 90 = North
        self.wp = wp
        
    def update(self, ins, use_numpy = False):
        """
        carry out the instruction ins
        """
        if ins[0] == 'N':
            self.wp[1] += int(ins[1:])
        elif ins[0] == 'S':
            self.wp[1] -= int(ins[1:])
        elif ins[0] == 'E':
            self.wp[0] += int(ins[1:])
        elif ins[0] == 'W':
            self.wp[0] -= int(ins[1:])
        elif ins[0] == 'F':
            self.pos[0] += self.wp[0] * int(ins[1:])
            self.pos[1] += self.wp[1] * int(ins[1:])
        elif ins[0] == 'L':
            if ins[1:] == '90':
                new_wp = [-self.wp[1], self.wp[0]]
            elif ins[1:] == '180':
                new_wp = [-self.wp[0], -self.wp[1]]
            elif ins[1:] == '270':
                new_wp = [self.wp[1], -self.wp[0]]
            else:
                print('unexpected instruction; ignoring')
                new_wp = self.wp
            self.wp = new_wp
        elif ins[0] == 'R':
            if ins[1:] == '90':
                new_wp = [self.wp[1], -self.wp[0]]
            elif ins[1:] == '180':
                new_wp = [-self.wp[0], -self.wp[1]]
            elif ins[1:] == '270':
                new_wp = [-self.wp[1], self.wp[0]]
            else:
                print('unexpected instruction; ignoring')
                new_wp = self.wp
            self.wp = new_wp
        else:
            print('instruction ignored')
            pass