with open('input.txt', 'r') as fobj:
    lines = fobj.read().split()
#
def get_symbol(i, j, lines):
    """
    gets the symbol at line i and column j
    """
    ii = i%len(lines)
    jj = j%len(lines[ii])
    return lines[ii][jj]

trees = 0
for i in range(len(lines)):
    j = 3*i
    if get_symbol(i, j, lines)=='#':
        trees += 1
with open('output.txt', 'w') as fobj:
    fobj.write(str(trees))
# part 2

slopes = [(1,1),
         (3,1),
         (5,1),
         (7,1),
         (1,2)]
def trees_encountered(slope, lines, verbose = False):
    right, down = slope
    trees = 0
    for i in range(0, len(lines), down):
        j = int(right*i/down)
        if verbose:
            print(i,j)
        if get_symbol(i, j, lines) == '#':
            trees += 1
    return trees

num_trees = list()
prod = 1
for slope in slopes:
    num_trees.append(trees_encountered(slope, lines))
    prod*=num_trees[-1]
#
with open('output2.txt', 'w') as fobj:
    fobj.write(str(prod))