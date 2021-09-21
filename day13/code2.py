# part 2
# I need to find the moment such that the wait time to see each listed bus is equal to its position in the list.
waittimes = dict()
for t,b in enumerate(lines[1].split(',')):
    if b!='x':
        waittimes[int(b)] = t
mods = {bus:(bus - t)%bus for bus, t in waittimes.items()}

def check_prime(n):
    for m in range(2,int(n/2)):
        if n%m == 0:
            return False
    return True
[check_prime(n) for n in mods.keys()]
N = 1
for bus in mods.keys():
    N*=bus
N

# do a sieve method!
mod = sorted(mods.items(), key = operator.itemgetter(0), reverse = True)

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

# fuck

# "direct method" via Bezout identity wtf :(