import math

def mid(low, high): return (low + high) // 2

def get_id(p):
    low, high = 0, 128
    for i in range(0, 7):
        if p[i] == "F": high = mid(low, high)
        else: low = mid(low, high)
    row = low
    low, high = 0, 8
    for i in range(7, 10):
        if p[i] == "L": high = mid(low, high)
        else: low = mid(low, high)
    col = low
    return row * 8 + col

def part1(raw_data):
    passes = [x for x in raw_data.split('\n')]
    highest = -math.inf
    return max([get_id(p) for p in passes])

def part2(raw_data):
    passes = [x for x in raw_data.split('\n')]
    ids = set([get_id(p) for p in passes])
    for i in ids:
        if i + 1 not in ids and i + 2 in ids:
            return i + 1
    