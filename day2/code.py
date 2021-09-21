with open('input.txt', 'r') as fobj:
    l = fobj.read().split('\n')

def count_occurences(letter, string):
    """
    counts how many times letter occurs in string
    """
    return sum([1 if lett == letter else 0 for lett in string])

def get_rule(s):
    """
    gets the rule out of an input line
    
    INPUT:
        s = a line of the input file
    
    OUTPUT:
        nmin = minimum number of occurrences
        nmax = maximum number of occurrences
        letter = letter in question
    """
    spl = s.split(' ')
    nrange = spl[0].split('-')
    nmin = eval(nrange[0])
    nmax = eval(nrange[1])
    letter = spl[1][0]
    return nmin, nmax, letter

def get_password(s):
    return s.split(' ')[-1]

def check_password(pw, nmin, nmax, letter):
    num = count_occurences(letter, pw)
    if nmin <= num and num <= nmax:
        return 1
    else:
        return 0
#
with open('output.txt','w') as fobj:
    fobj.write(str(sum([check_password(get_password(s), *get_rule(s)) for s in l[:-1]])))
    
# now second part
def check_password_part2(pw, a, b, letter):
    if pw[a-1] == letter and pw[b-1]!=letter:
        return 1
    elif pw[a-1] != letter and pw[b-1]==letter:
        return 1
    else:
        return 0

with open('output2.txt', 'w') as fobj:
    fobj.write(str(sum([check_password_part2(get_password(s), *get_rule(s)) for s in l[:-1]])))

