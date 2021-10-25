from code import Node

def get_baselevel_times(string):
    level = 0
    for i, s in enumerate(string):
        if s == '(':
            level += 1
        elif s == ')':
            level -= 1
        if level == 0 and s == '*':
            return i
    return False

def get_baselevel_plus(string):
    level = 0
    for i, s in enumerate(string):
        if s == '(':
            level += 1
        elif s == ')':
            level -= 1
        if level == 0 and s == '+':
            return i
    return False

def remove_outer_parens(string):
    if string[0] != '(':
        return string
    level = 1
    pos = 1
    matched = False
    while not matched:
        if string[pos] == '(':
            level += 1
        elif string[pos] == ')':
            level -= 1
        if level == 0:
            matched = True
        pos += 1
    if pos == len(string):
        return string[1:-1]
    else:
        return string

times = lambda x, y : x*y
plus = lambda x, y : x+y

def create_node(string):
    string = remove_outer_parens(string)
    i = get_baselevel_times(string)
    if i:
        return Node(create_node(string[:i]), create_node(string[i+1:]), times, None)
    i = get_baselevel_plus(string)
    if i:
        return Node(create_node(string[:i]), create_node(string[i+1:]), plus, None)
    return Node(None, None, None, eval(string[0]))

if __name__ == '__main__':
    # do stuff
    with open('input.txt', 'r') as fobj:
        lines = fobj.read().split('\n')
    exprs = [list(line.replace(' ', '')) for line in lines[:-1]]

    answer = 0
    for string in exprs:
        node = create_node(string)
        answer += node.get_value()
    
    with open('output2.txt', 'w') as fobj:
        fobj.write(str(answer))

    with open('Dmitry-p18.txt','r') as fobj:
        lines = fobj.read().split('\n')
    exprs = [list(line.replace(' ','')) for line in lines[:-1]]

    answers = [str(create_node(string).get_value()) for string in exprs]
    with open('dmitry-treats.txt','w') as fobj:
        fobj.write('\n'.join(answers))
