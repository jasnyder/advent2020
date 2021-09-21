with open('input.txt', 'r') as fobj:
    lines = fobj.read().split('\n')

def apply_mask(num, mask):
    """
    takes the number to be set into memory, and applies the mask
    
    INPUT:
        num = int
        mask = string of 0/1/X
    """
    import numpy as np
    num_b = np.binary_repr(num, width = len(mask))
    out_b = [int(M) if M in ['0','1'] else int(N) for N, M in zip(num_b, mask)]
    return sum([out_b[k]*2**(len(mask)-k-1) for k in range(len(mask))])

mem = dict()

for line in lines:
    if line == '':
        pass
    elif line.split()[0] == 'mask':
        current_mask = line.split()[-1]
    else:
        num = int(line.split()[-1])
        idx = line.split()[0][4:-1]
        new_num = apply_mask(num, current_mask)
        mem[idx] = new_num
with open('output.txt','w') as fobj:
    fobj.write(str(sum(mem.values())))
    
# part 2
# this is going to be very messy

def mask_address(address, mask):
    """
    returns a whole set of addresses that come from applying the mask
    
    INPUT:
        address = str
        mask = string of 0/1/X
    """
    import numpy as np
    add_bin = np.binary_repr(int(address), width = len(mask))
    address_template = [A if M == '0' else M for A, M in zip(add_bin, mask)]
    num_floating = sum([c=='X' for c in address_template])
    return address_template

def fix_floating_bits(address, addr_list = None):
    if addr_list is None:
        addr_list = list()
    if 'X' in address:
        i = address.index('X')
        a1 = list(address).copy()
        a1[i] = '0'
        a2 = list(address).copy()
        a2[i] = '1'
        fix_floating_bits(a1, addr_list = addr_list)
        fix_floating_bits(a2, addr_list = addr_list)
    else:
        addr_list.append(address)
    return addr_list

def get_int(address):
    L = len(address)
    return sum([2**(L-k-1)*int(address[k]) for k in range(L)])

mem = dict()

for line in lines:
    if line == '':
        pass
    elif line.split()[0] == 'mask':
        current_mask = line.split()[-1]
    else:
        num = int(line.split()[-1])
        idx = line.split()[0][4:-1]
        addr_list = fix_floating_bits
        address = mask_address(idx, current_mask)
        addr_list = fix_floating_bits(address)
        for addr in addr_list:
            mem[get_int(addr)]=num
with open('output2.txt','w') as fobj:
    fobj.write(str(sum(mem.values())))