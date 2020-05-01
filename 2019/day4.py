def is_valid(i, adjacent_limit):
    s = str(i)
    if len(s) != 6:
        return False
    for a, b in zip(s, sorted(s)):
        if a != b:
            return False
    has_adj = False
    for i in map(str, range(1, 10)):
        left = s.find(i)
        right = s.rfind(i)
        if right != -1 and left != -1:
            if adjacent_limit and right - left == 1:
                has_adj = True
            elif not adjacent_limit and right - left > 0:
                has_adj = True
    return has_adj


def count_passwords(a, b, adjacent_limit=False):
    total = 0
    for i in range(a, b):
        total += 1 if is_valid(i, adjacent_limit) else 0
    return total


f = open('day4.txt')
a, b = map(int, f.read().strip().split('-'))


def partOne():
    return count_passwords(a, b)


def partTwo():
    return count_passwords(a, b, True)


print('Part 1:', partOne())
print('Part 2:', partTwo())
