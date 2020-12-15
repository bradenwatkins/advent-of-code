def is_in_range(num, low, high):
    if not num.isnumeric(): return False
    num = int(num)
    return low <= num and num <= high


def byr(value):
    return is_in_range(value, 1920, 2002)


def iyr(value):
    return is_in_range(value, 2010, 2020)


def eyr(value):
    return is_in_range(value, 2020, 2030)


def hgt(value):
    if value.endswith('cm'):
        return is_in_range(value[:-2], 150, 193)
    if value.endswith('in'):
        return is_in_range(value[:-2], 59, 76)
    return False


def hcl(value):
    if not value.startswith("#"): return False
    if len(value[1:]) != 6: return False
    try:
        int(value[1:], 16)
    except ValueError:
        return False
    return True


def ecl(value):
    eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return value in eye_colors


def pid(value):
    return value.isnumeric() and len(value) == 9


validators = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid
}


def check_passport(passport):
    return 

def parse(raw_data):
    passports = list()
    lines = [x.strip() for x in raw_data.split('\n\n')]
    for line in lines:
        passport = dict()
        for field in [f.strip().split(':') for f in line.split()]:
            passport[field[0]] = field[1]
        passports.append(passport)
    return passports

def part1(raw_data):
    valid = 0
    for p in parse(raw_data):
        if all([key in p for key, _ in validators.items()]):
            valid += 1
    return valid


def part2(raw_data):
    valid = 0
    for p in parse(raw_data):
        if all([key in p and valid(p[key]) for key, valid in validators.items()]):
            valid += 1
    return valid
