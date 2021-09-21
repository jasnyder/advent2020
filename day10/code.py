with open('input.txt', 'r') as fobj:
    nums = [int(x) for x in fobj.read().split()]
nums

"""
I need to spend some time parsing this question.
Each line in the input (nums) is a rating for OUTPUT JOLTAGE of an adapter
I also have a BUILT-IN INPUT ADAPTER rated for 3+max(nums)
"""
nums_sorted = sorted(nums)
diffs = [nums_sorted[i+1] - nums_sorted[i] for i in range(len(nums)-1)]
num_onediffs = sum([d == 1 for d in diffs]) + 1
num_threediffs = sum([d==3 for d in diffs]) + 1

ans = num_onediffs* num_threediffs

with open('output.txt', 'w') as fobj:
    fobj.write(str(ans))

#
nums = nums_sorted

"""
part 2 - I need to find a way to encode and enumerate all the possible valid sequences of adapters
"""
(max(nums) - min(nums))/3
"""
aahh!! I can just work directly with the sequence of differences. The sequence of differences fully specifies the sequence of adapters. And whenever there are, say, 2 1-diffs in a row, i can replace that with a 2-diff.

any string of 3-diffs cannot be reduced. so really i just need to think of the strings of 1-diffs!!
If I figure out how many valid sequences I can make out of a length-L run of 1-diffs, then I have the answer!

Can I compute that number recursively?
If I have L+1 1-diffs, I can:
"""
def N(L):
    if L==0:
        return 1
    elif L==1:
        return 1
    elif L==2:
        return 2
    else:
        return N(L-1)+N(L-2)+N(L-3)
# it's the Tribonacci numbers! OEIS to the rescue!
def run_lengths(diffs):
    lengths = list()
    run = False
    l = 1
    for i, d in enumerate(diffs):
        
        if d==1 and not run:
            run = True
            l += 1
            if i==len(diffs)-1:
                lengths.append(l)
        elif d==1 and run:
            l += 1
            if i==len(diffs)-1:
                lengths.append(l)
        elif d==3 and run:
            lengths.append(l)
            run = False
            l = 0
        else:
            pass
    return lengths
lengths = run_lengths(diffs)

ans = 1
for L in lengths:
    ans *= N(L)
with open('output2.txt', 'w') as fobj:
    fobj.write(str(ans))