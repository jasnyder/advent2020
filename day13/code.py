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
    
# part 2

waittimes = dict()
for t,b in enumerate(lines[1].split(',')):
    if b!='x':
        waittimes[int(b)] = t
mods = {bus:(bus - t)%bus for bus, t in waittimes.items()}

mod = sorted(mods.items(), key = operator.itemgetter(0), reverse = True)

def check(now, waittimes):
    return all([bus - now%bus == t for bus, t in waittimes.items()])

maxit = 1e8
its = 0
T = mod[0][1]
n = mod[0][0]
step = 0
done = False
while not done and its < maxit:
    its+=1
    k = 0
    subdone = False
    while not subdone:
        subdone = (T%mod[step][0] == mod[step][1])
        T += n
        k += 1
    n *= k
    step+=1
    T += mod[step][1]
    done = check(T, waittimes)
print(T)

