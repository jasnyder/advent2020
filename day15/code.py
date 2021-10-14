with open('input.txt','r') as fobj:
    raw = fobj.read().split(',')
    nums = [int(n) for n in raw]

# reverse the list to take advantage of the builtin .index() method of lists
nums.reverse()

while len(nums)<2020:
    last_spoken = nums[0]
    try:
        i = nums[1:].index(last_spoken)
        next_spoken = i + 1
    except ValueError:
        next_spoken = 0
    
    nums.insert(0, next_spoken)

with open('output1.txt','w') as fobj:
    fobj.write(str(nums[0]))

"""
I need to be smarter about this to get to the 30000000th number spoken...

What if I just keep track of it in a dictionary:
time_since[i] = #
"""
with open('input.txt','r') as fobj:
    raw = fobj.read().split(',')
    nums = [int(n) for n in raw]

def update(last_spoken, turn, num):
    """
    updates the last_spoken dictionary
    returns True if the new number was spoken previously
    returns False if the new number was never spoken before
    """
    if num in last_spoken.keys():
        last_spoken[num].append(turn+1)
        while len(last_spoken[num]) > 2:
            last_spoken[num].pop(0)
        return True
    else:
        last_spoken[num] = [turn+1]
        return False

last_spoken = dict()
for turn, num in enumerate(nums[:-1]):
    update(last_spoken, turn, num)

current_num = nums[-1]
turn = len(nums) - 1

while turn < 30000000 - 1:
    not_new = update(last_spoken, turn, current_num)
    if not_new:
        current_num = last_spoken[current_num][1] - last_spoken[current_num][0]
    else:
        current_num = 0
    turn += 1


with open('output2.txt','w') as fobj:
    fobj.write(str(current_num))