with open('input.txt', 'r') as fobj:
    x = fobj.read()
#
passports = x.split('\n\n')

def to_dict(passport):
    fields = passport.split()
    d = dict()
    for field in fields:
        key, value = field.split(':')
        d[key] = value
    return d

passport_dicts = [to_dict(p) for p in passports]

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

def check_dict(d, req = ['byr','iyr','eyr','hgt','hcl','ecl','pid']):
    return all([r in d.keys() for r in req])

num_valid = sum([check_dict(d) for d in passport_dicts])
with open('output.txt', 'w') as fobj:
    fobj.write(str(num_valid))
# part2

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
def check_dict2(d):
    if not check_dict(d):
        return False
    # check byr
    try:
        byr = int(d['byr'])
        if (byr<1920) or (byr>2002):
            return False
    except ValueError:
        return False
    # check iyr
    try:
        iyr = int(d['iyr'])
        if (iyr<2010) or (iyr>2020):
            return False
    except ValueError:
        return False
    # check eyr
    try:
        eyr = int(d['eyr'])
        if (eyr<2020) or (eyr>2030):
            return False
    except ValueError:
        return False
    # check hgt
    if d['hgt'][-2:] not in ['in', 'cm']:
        return False
    hgt = int(d['hgt'][:-2])
    if d['hgt'][-2:]=='in':
        if (hgt<59) or (hgt>76):
            return False
    elif d['hgt'][-2:]=='cm':
        if (hgt<150) or (hgt>193):
            return False
    # check hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    intchars = [str(i) for i in range(10)]
    athruf = ['a','b','c','d','e','f']
    hcl = d['hcl']
    if len(hcl)!=7:
        return False
    if hcl[0] != '#' or not all([x in intchars or x in athruf for x in hcl[1:]]):
        return False
    # check ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if d['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(d['pid'])!=9 or not all([x in intchars for x in d['pid']]):
        return False
    # if you've made it this far...
    return True

num_valid2 = sum([check_dict2(d) for d in passport_dicts])
with open('output2.txt','w') as fobj:
    fobj.write(str(num_valid2))