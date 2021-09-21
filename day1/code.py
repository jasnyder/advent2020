fobj = open('input.txt', 'r')
s = fobj.read()
fobj.close()
l = [eval(n) for n in s.split()]

def f(l):
    for i, x in enumerate(l):
        for y in l[:i]:
            if x+y == 2020:
                return x*y
    return "shit!!!"

with open('output.txt', 'w') as fobj:
    fobj.write(str(f(l)))
    
def g(l):
    L = len(l)
    for i in range(L):
        for j in range(i):
            for k in range(j):
                if l[i] + l[j] + l[k] == 2020:
                    return l[i] * l[j] * l[k]
    return "shit!!!!!!"

with open('output2.txt', 'w') as fobj:
    fobj.write(str(g(l)))