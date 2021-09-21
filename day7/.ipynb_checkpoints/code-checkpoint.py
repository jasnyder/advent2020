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

D['dotted yellow']
D['light black'].keys()
