# Part 1

To complete this puzzle I need to figure out a systematic way of parsing lines of input. In terms of evaluation, what I want to arrive at is a binary-tree representation of each expression. The rules of left-precedence will, I think, make this pretty straightforward to evaluate.

What does my binary tree rep'n need to do? Each node represents the combination of two other nodes. Attributes a node should have:
* left child
* right child
* operation (+ or *)
* value (i.e. numerical result of the calculation)

I'll also need a way for nodes to compute their value. Something like
```python
class Node:
    def __init__(self, left, right, op, value = None):
        self.left = left        //Node
        self.right = right      //Node
        self.op = op            //fun: (int, int) -> int
        self.value = value      //int

    def get_value(self):
        if self.value is None:
            self.evaluate()
        return self.value

    def evaluate(self):
        if self.value is None:
            self.value = self.op(self.left.get_value(), self.right.get_value())
        else:
            pass
```

This should work right?

Now I need to think about how to generate a binary tree out of the string (or list) representation given in the input.

I'm thinking that I should have a method that creates a `Node` from a string, and this method will run recursively. That is, I'll pass the full string to the root node, and it will figure out where to divide the string, then pass the sub-strings to the same method to create its left- and right-children.

An interesting note here: as I'm thinking about it, this will create the tree from the top down. If that's so, then I should really start from the *right* side of the input string, so that the left-most members are leaf nodes that will get combined first before being passed up to the righter-more members. I think I can get around this by simply reversing the whole expression to start LOL.

This is a bit complicated due to parentheses

```python
def plus(x, y):
    return x+y
def times(x, y):
    return x*y

def create_node(stringexp):
    '''
    this function creates nodes recursively to represent the arithmetic expression as a binary tree
    NOTE: this function does RIGHT-precedence, i.e. evaluates the right-most expression first, aside from parentheses
    Therefore you should reverse the given arithmetic string before passing it in
    '''
    if len(stringexp)==1:
        node = Node(None, None, None, eval(stringexp[0]))
        return node

    if stringexp[0] == '(':
        level = 1
        pos = 0
        while level > 0:
            pos += 1
            if stringexp[pos] == '(':
                level += 1
            elif stringexp[pos] == '}':
                level -= 1
        leftstr = stringexpr[1:pos]
    else:
        leftstr = stringexpr[0]
        pos = 1
    rightstr = stringexpr[pos+1:]

    if stringexpr[pos] == '+':
        op = plus
    elif stringexpr[pos] == '*':
        op = times
    
    return Node(create_node(leftstr), create_node(rightstr), op, None)
```

# Part 2

Now I need to make `+` and `*` have different precedence levels - addition gets carried out before multiplication. In other words, multiplication gets carried out after addition.

I think my approach will still be to construct a tree that will be evaluated from the bottom up - so I always need to make sure that mutliplication is after (higher in the tree) than addition. This will require being more aware of the whole string than I was in Part 1.

Let's think about what different ways an arithmetic expression can look. For example:
```
4 + (5 + (5 * 5 + 3 + 2) + (6 + 4 * 9 * 2 * 8) * 6 + (7 * 5 * 2) * (2 * 8 * 2)) + (8 * 7 + 7) * 6 * 9 * (5 + 9)
```
This line has six atoms, separated by five operators: `+, +, *, *, *`. I need to split these atoms up across levels of a binary tree. It doesn't matter what exact order I use as long as the `+`'s are below the `*`'s. So I might as well just split on the first `*` I see that's not inside parans

```python
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
        # look for a * at level-0
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
```
