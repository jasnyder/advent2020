with open('input.txt','r') as fobj:
    raw = fobj.read()

rule_specs, mine, theirs = raw.split('\n\n')

rule_specs = rule_specs.split('\n')

mine = [int(x) for x in mine.split()[-1].split(',')]
others = [[int(x) for x in y.split(',')] for y in theirs.split('\n')[1:-1]]

def checker(range1, range2):
    l1, u1 = range1
    l2, u2 = range2
    return lambda x : ((l1 <= x) and (x <= u1)) or ((l2 <= x) and (x <= u2))

rules = list()
for spec in rule_specs:
    range1 = spec.split()[-3].split('-')
    range2 = spec.split()[-1].split('-')
    range1 = list(map(int, range1))
    range2 = list(map(int, range2))
    rules.append(checker(range1, range2))

"""
Now I should look through all the nearby tickets and identify those values not valide for any rule
I will keep these invalid values in a list, and the answer is their sum
"""

invalid_values = list()
for ticket in others:
    for num in ticket:
        if not any([rule(num) for rule in rules]):
            invalid_values.append(num)

with open('output1.txt', 'w') as fobj:
    fobj.write(str(sum(invalid_values)))

"""
Part 2
Discard all invalid tickets and use the remaining ones to figure out which field is which

there are 20 fields and 20 rules
"""

valid_others = list()
for ticket in others:
    valid = True
    for num in ticket:
        if not any([rule(num) for rule in rules]):
            valid = False
    if valid:
        valid_others.append(ticket)
"""
Approach: disqualify fields one at a time
Go through the tickets, and for each ticket:
    - look at each field. for each field on the ticket:
        - determine which rules it does and doesn't satisfy
          rules not satisfied by that field cannot correspond
"""
possible_field_IDs = [list(range(20)) for _ in range(20)]
"""
possible_field_IDs[i] = list of all rule indices that could correspond to field i
"""

for i in range(20):
    for j in range(20):
        if not all([rules[j](ticket[i]) for ticket in valid_others]):
            possible_field_IDs[i].remove(j)

"""
Now I need to do process of elimination!
"""
def eliminate(possible_field_IDs):
    did_something = False
    for i, ID in enumerate(possible_field_IDs):
        if len(ID) == 1:
            for k, alter in enumerate(possible_field_IDs):
                if i!=k:
                    try:
                        alter.remove(ID[0])
                        did_something=True
                    except ValueError:
                        pass
    return did_something

done = False
while not done:
    done = not eliminate(possible_field_IDs)

answer = 1
for i, num in enumerate(mine):
    if rule_specs[possible_field_IDs[i][0]].split()[0]=='departure':
        answer *= num

with open('output2.txt', 'w') as fobj:
    fobj.write(str(answer))