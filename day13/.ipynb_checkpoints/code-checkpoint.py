with open('input.txt', 'r') as fobj:
    lines = fobj.read().split('\n')[:-1]
now = int(lines[0])

int(now/17)
buses = list()
for b in lines[1].split(','):
    if b!='x':
        buses.append(int(b))
buses

waittimes = dict()
for bus in buses:
    waittimes[bus] = bus - now%bus
import operator
bus, waittime = sorted(waittimes.items(), key = operator.itemgetter(1))[0]
ans = bus * waittime
with open('output.txt', 'w') as fobj:
    fobj.write(str(ans))
    
