with open('input.txt','r') as fobj:
    seats = fobj.read().split('\n')[:-1]

"""
This is a cellular automaton with three states: '.', 'L', '#'

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
"""


def pre_neighbors(i,j):
    return [(i+1, j),
            (i, j+1),
            (i-1, j),
            (i, j-1),
            (i+1, j+1),
            (i-1, j+1),
            (i-1, j-1),
            (i+1, j-1)]
def trim_neighbors(nbhd, width=width, height=height):
    out = list()
    for (i, j) in nbhd:
        if j in range(width) and i in range(height):
            out.append((i,j))
    return out

def count_occupied(i,j, seats,**kwargs):
    # use kwargs to pass in width, height if needed
    nbhd = trim_neighbors(pre_neighbors(i,j), **kwargs)
    return sum([seats[i][j]=='#' for i,j in nbhd])

def update(seats):
    # initialize a new list of lists to contain the future state
    seats_new = [[None for y in x] for x in seats]
    h = len(seats)
    w = len(seats[0])
    changed = False
    for i in range(height):
        for j in range(width):
            if seats[i][j] =='L' and count_occupied(i, j, seats, width=w, height=h)==0:
                seats_new[i][j] = '#'
                changed = True
            elif seats[i][j]=='#' and count_occupied(i, j, seats, width=w, height=h) >=4:
                seats_new[i][j] = 'L'
                changed = True
            else:
                seats_new[i][j] = seats[i][j]
    return seats_new, changed

def count_total(seats):
    total = 0
    for row in seats:
        for seat in row:
            if seat=='#':
                total+=1
    return total

done = False
while not done:
    seats, changed = update(seats)
    done = not changed
    
ans = count_total(seats)
with open('output.txt', 'w') as fobj:
    fobj.write(str(ans))

# part 2
# now they care about the first visible seat in each of the eight directions
with open('input.txt','r') as fobj:
    seats = fobj.read().split('\n')[:-1]


def validate(i, j):
    if i in range(height) and j in range(width):
        return True
    else:
        return False
dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
def visible_seats(i, j, seats, dirs = dirs):
    out = list()
    for di, dj in dirs:
        step = 1
        found = False
        while validate(i+step*di, j+step*dj) and not found:
            if seats[i+step*di][j+step*dj] != '.':
                out.append(seats[i+step*di][j+step*dj])
                found = True
            else:
                step += 1
    return out

def count_visible(i, j, seats):
    vis = visible_seats(i, j, seats)
    return sum([x =='#' for x in vis])

def update2(seats):
    # initialize a new list of lists to contain the future state
    seats_new = [[None for y in x] for x in seats]
    h = len(seats)
    w = len(seats[0])
    changed = False
    for i in range(height):
        for j in range(width):
            if seats[i][j] =='L' and count_visible(i, j, seats)==0:
                seats_new[i][j] = '#'
                changed = True
            elif seats[i][j]=='#' and count_visible(i, j, seats) >=5:
                seats_new[i][j] = 'L'
                changed = True
            else:
                seats_new[i][j] = seats[i][j]
    return seats_new, changed

done = False
while not done:
    seats, changed = update2(seats)
    done = not changed
ans = count_total(seats)
with open('output2.txt', 'w') as fobj:
    fobj.write(str(ans))
