"""
This puzzle is to simulate a 3D game of life. The input is a 2D slice of initial conditions
Sites are assumed to be inactive unless otherwise specified. That makes me think a dictionary will work well, where keys are sites and I query with .get(site, 0)

A wrinkle here: I need to consider sites that are not already mentioned.
That is, I might need to activate sites that are not in grid.keys()
"""
grid = dict()
with open('input.txt', 'r') as fobj:
    lines = fobj.read().split('\n')
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            grid[(i,j,0)] = 1 if symbol == '#' else 0


# This may be overkill but I'm going to explicitly write out (with help
# of this string_gen function) the 26 neighbor sites of any given (i, j, k)
# This avoids the if-not-all-zero check that would otherwise be needed 27
# times per function call
def neighbors_string_gen():
    nbrs = list()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if not all([d==0 for d in [dx, dy, dz]]):
                    nbrs.append(f'(i+{dx}, j+{dy}, k+{dz})')
    return nbrs

nbrs = neighbors_string_gen()

@functools.lru_cache(maxsize=1000, typed=False)
def neighborhood(site):
    i, j, k = site
    return [(i+-1, j+-1, k+-1),(i+-1, j+-1, k+0),(i+-1, j+-1, k+1),
            (i+-1, j+0, k+-1),(i+-1, j+0, k+0),(i+-1, j+0, k+1),
            (i+-1, j+1, k+-1),(i+-1, j+1, k+0),(i+-1, j+1, k+1),
            (i+0, j+-1, k+-1),(i+0, j+-1, k+0),(i+0, j+-1, k+1),
            (i+0, j+0, k+-1),(i+0, j+0, k+1),(i+0, j+1, k+-1),
            (i+0, j+1, k+0),(i+0, j+1, k+1),(i+1, j+-1, k+-1),
            (i+1, j+-1, k+0),(i+1, j+-1, k+1),(i+1, j+0, k+-1),
            (i+1, j+0, k+0),(i+1, j+0, k+1),(i+1, j+1, k+-1),
            (i+1, j+1, k+0),(i+1, j+1, k+1)]

def update(grid):
    # make a set of sites to update. this will include sites not already in grid.keys()
    # the extra sites will always be neighbors of known sites
    to_update = dict()
    for site in grid.keys():
        to_update[site] = 0
        for neighbor in neighborhood(site):
            to_update[neighbor] = 0
    for site in to_update.keys():
        n_active = sum([grid.get(neighbor, 0) for neighbor in neighborhood(site)])
        if grid.get(site, 0)==0 and n_active==3:
            to_update[site] = 1
        elif grid.get(site, 0)==1 and n_active in [2,3]:
            to_update[site] = 1
    grid.update(to_update)
    return

steps = 0
while steps < 6:
    update(grid)
    steps += 1

answer = sum(grid.values())
with open('output1.txt','w') as fobj:
    fobj.write(str(answer))
    
"""
Part 2! Now do FOUR dimensions! lmao
This shouldn't be too crazy. just modify the neighborhood function
"""

# I think generating the string of the function was really unnecessary
# I can just remove the site manually before returning the neighborhood
@functools.lru_cache(maxsize=1000, typed=False)
def neighborhood_4d(site):
    i, j, k, l = site
    out = list()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz  in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    out.append((i+dx, j+dy, k+dz, l+dw))
    out.remove(site)
    return out


def update_4d(grid):
    # make a set of sites to update. this will include sites not already in grid.keys()
    # the extra sites will always be neighbors of known sites
    to_update = dict()
    for site in grid.keys():
        to_update[site] = 0
        for neighbor in neighborhood_4d(site):
            to_update[neighbor] = 0
    for site in to_update.keys():
        n_active = sum([grid.get(neighbor, 0) for neighbor in neighborhood_4d(site)])
        if grid.get(site, 0)==0 and n_active==3:
            to_update[site] = 1
        elif grid.get(site, 0)==1 and n_active in [2,3]:
            to_update[site] = 1
    grid.update(to_update)
    return

# Reload the initial condition grid
grid = dict()
with open('input.txt', 'r') as fobj:
    lines = fobj.read().split('\n')
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            grid[(i,j,0,0)] = 1 if symbol == '#' else 0

steps = 0
while steps < 6:
    update_4d(grid)
    steps += 1

answer = sum(grid.values())
with open('output2.txt','w') as fobj:
    fobj.write(str(answer))