class Node:
    def __init__(self, left, right, op, value = None):
        self.left = left        # Node
        self.right = right      # Node
        self.op = op            # fun: (int, int) -> int
        self.value = value      # int

    def get_value(self):
        if self.value is None:
            self.value = self.op(self.left.get_value(), self.right.get_value())
        else:
            pass
        return self.value


def create_node(stringexp):
    '''
    this function creates nodes recursively to represent the arithmetic expression as a binary tree
    '''
    if len(stringexp)==1:
        # this is a leaf node, all we need to know is its value
        node = Node(None, None, None, eval(stringexp[0]))
        return node

    if stringexp[-1] == ')':
        # find the matching left-paren by stepping backwards
        # keep track of the "level", how many open parens we've seen
        level = 1
        pos = -1
        while level > 0:
            pos -= 1
            if stringexp[pos] == ')':
                level += 1
            elif stringexp[pos] == '(':
                level -= 1
        if pos == -len(stringexp):
            # in this case the whole expression is enclosed in parens; re-call the function after stripping parens away
            return create_node(stringexp[1:-1])
        else:
            rightstr = stringexp[pos+1:-1]
        # at this point pos is the index of the left-most character in the right-hand string
        # therefore the operation symbol is at index pos-1
    else:
        rightstr = stringexp[-1]
        pos = -1
    leftstr = stringexp[:pos-1]

    if stringexp[pos-1] == '+':
        op = lambda x, y : x+y
    elif stringexp[pos-1] == '*':
        op = lambda x, y : x*y
    else:
        print(stringexp, pos-1)
        return
    
    return Node(create_node(leftstr), create_node(rightstr), op)

with open('input.txt', 'r') as fobj:
    lines = fobj.read().split('\n')
exprs = [list(line.replace(' ', '')) for line in lines[:-1]]


answer = 0
for expr in exprs:
    answer += create_node(expr).get_value()

with open('output1.txt','w') as fobj:
    fobj.write(str(answer))


"""
Now I need to do it a different way; rather than order taking precedence, it's determined by which operation it is
Plus gets evaluated before times

So, what I need to do is to go through the string, and find all the timeses

whenever I find a times, I can split that into two leaves
"""