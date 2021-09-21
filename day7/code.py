with open('input.txt','r') as fobj:
    rules_raw = fobj.read().split('\n')
#
len(rules_raw)
"""
Hmm.. how to represent the data?
This feels like a weighted tree. I'd rather not import networkx or anything. I think i can do this with just nested dicts:

D[typeA][typeB] is the number of typeB bags that go into a typeA bag.

Said differently, D[typeA] is a dictionary that tells what bags have to go inside a typeA bag
"""

def rule_dict(rule):
    """
    This function takes a raw rule (line of input) and produces a dictionary that encodes that rule.
    
    the output is a dictionary whose key is the bag type whose contents are described by the rule, and whose value is a dictionary listing the number of each other type of bag inside of it.
    """
    d = dict()
    typeA = rule.split(' bags')[0]
    if 'no other' in rule:
        return {typeA:{}}
    try:
        contains = rule.split('contain ')[1].split(', ')
    except IndexError:
        print(rule)
        return {}
    for cont in contains:
        num = int(cont[0])
        typeB = cont.split(' bag')[0][2:]
        d[typeB] = num
    return {typeA:d}

d = dict()
for rule in rules_raw:
    d.update(rule_dict(rule))
#

"""
This dictionary doesn't directly give me what I want.... I want the opposite.
"""
def flip_dict(d):
    """
    turns the dict upside down...
    
    D[typeB][typeA] = the number of typeB bags that go in a typeA bag.
    """
    D = dict()
    for typeA in d.keys():
        for typeB, num in d[typeA].items():
            if typeB in D.keys():
                D[typeB].update({typeA:num})
            else:
                D[typeB] = {typeA:num}
    return D

D = flip_dict(d)

flatten = lambda t: [item for sublist in t for item in sublist]

def get_parents(typeB, D):
    """
    gets the types of bags that can contain a typeB bag
    
    if recursive, it also returns the types of bags that can contain those bags, etc.
    """
    return list(D[typeB].keys()) + flatten([get_parents(typeA, D) if typeA in D.keys() else [] for typeA in D[typeB].keys()])

pts = get_parents('shiny gold', D)
num_unique = len(set(pts))
with open('output.txt', 'w') as fobj:
    fobj.write(str(num_unique))
    
# part 2
# how many individual bags are required inside a single shiny gold bag?
# I need to count with the numbers in the dictionary

def count_bags(typeA, d):
    """
    counts the number of bags required inside a single typeA bag, according to the nesting defined in the dictionary d
    """
    if d[typeA] == {}:
        return 0
    else:
        return sum([num * (count_bags(typeB, d)+1) for typeB, num in d[typeA].items()])

total_bags = count_bags('shiny gold', d)
with open('output2.txt', 'w') as fobj:
    fobj.write(str(total_bags))