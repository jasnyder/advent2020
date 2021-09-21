with open('input.txt', 'r') as fobj:
    codes = fobj.read().split()
def get_coords(code):
    fb = code[:7]
    lr = code[7:]
    row = sum([2**(6-i) if l=='B' else 0 for (i, l) in enumerate(fb)])
    col = sum([2**(2-i) if l=='R' else 0 for (i, l) in enumerate(lr)])
    return row, col

def get_index(row, col):
    return 8*row + col

indices = [get_index(*get_coords(code)) for code in codes]

with open('output.txt', 'w') as fobj:
    fobj.write(str(max(indices)))
    
# part 2. find the missing ID: the one that's missing but whose neighbors are both there.
sorted_IDs = sorted(indices)
sorted_IDs
missing_idx = [a - b for a, b in zip(sorted_IDs[1:], sorted_IDs[:-1])].index(2)
with open('output2.txt','w') as fobj:
    fobj.write(str(sorted_IDs[missing_idx]+1))
