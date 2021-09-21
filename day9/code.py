with open('input.txt','r') as fobj:
    nums = [int(x) for x in fobj.read().split()]
#
nums

def is_sum(num, preamble):
    for y in preamble:
        if num-y in preamble:
            return True
    return False

def find_first_bad(nums, length = 25):
    for j in range(length, len(nums)):
        if not is_sum(nums[j], nums[j-length:j]):
            return nums[j]
    return 'no baddies!'


with open('output.txt', 'w') as fobj:
    fobj.write(str(find_first_bad(nums)))
    
N = find_first_bad(nums)

# part 2
# find a contiguous range of numbers that sum to the baddie
# search through the list... first for the lower index, then for the upper index

def find_contiguous(nums, N):
    for i in range(len(nums)):
        j = i+1
        while sum(nums[i:j]) < N:
            j += 1
        if sum(nums[i:j]) == N:
            return nums[i:j]
    return 'i didn\'nt find it!!'

contig = find_contiguous(nums, N)

ans = min(contig)+max(contig)
with open('output.txt', 'w') as fobj:
    fobj.write(str(ans))