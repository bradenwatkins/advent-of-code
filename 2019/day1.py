def deepsum(num):
    return 0 if num < 0 else num + deepsum(num // 3 - 2)


f = open('day1.txt')
weights = [int(line) for line in f.read().strip().split('\n')]


def partOne():
    return sum([w // 3 - 2 for w in weights])


def partTwo():
    return sum([deepsum(w // 3 - 2) for w in weights])


print('Part 1:', partOne())
print('Part 2:', partTwo())
