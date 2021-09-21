with open('input.txt', 'r') as fobj:
    groups_raw = fobj.read().split('\n\n')
    groups = [group.split() for group in groups_raw]
len(groups)

"""
Each group in groups is effectively a dictionary: the index into group specifies the person, and the value gives a list of all the questions they answered yes to.

I'll change the representation now: I'll make a dictionary whose keys are the questions, and whose values are a list of person indices who answered yes to them
"""
def question_dict(group):
    d = dict()
    for personID, answers in enumerate(group):
        for a in answers:
            if a in d.keys():
                d[a].append(personID)
            else:
                d[a] = [personID]
    return d

total = sum([len(question_dict(group)) for group in groups])
with open('output.txt', 'w') as fobj:
    fobj.write(str(total))
    
# part 2
# count the number of questions to which everyone answered yes
def list_unanimous(group):
    l = list()
    for answer in group[0]:
        if all([answer in answers for answers in group]):
            l.append(answer)
    return l

total2 = sum([len(list_unanimous(group)) for group in groups])
with open('output2.txt', 'w') as fobj:
    fobj.write(str(total2))