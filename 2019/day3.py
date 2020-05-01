import math


def follow(path):
    x, y = 0, 0
    s = 0
    coords = set()
    steps = dict()
    for step in path:
        d = step[0]
        dist = int(''.join(step[1:]))
        for _ in range(dist):
            if d == 'U' or d == 'D':
                y += 1 if d == 'U' else -1
            if d == 'R' or d == 'L':
                x += 1 if d == 'R' else -1
            coords.add((x, y))
            s += 1
            key = str(x) + str(y)
            if key not in steps:
                steps[key] = s
    return coords, steps


def solve(p1, p2):
    coords1, _ = follow(p1)
    coords2, _ = follow(p2)
    intersections = coords1.intersection(coords2)
    min_dist = math.inf
    for i in intersections:
        dist = abs(i[0]) + abs(i[1])
        if dist != 0 and dist < min_dist:
            min_dist = dist
    return min_dist


def time_sensitive(p1, p2):
    coords1, steps1 = follow(p1)
    coords2, steps2 = follow(p2)
    intersections = coords1.intersection(coords2)
    min_steps = math.inf
    for x, y in intersections:
        key = str(x) + str(y)
        steps = steps1[key] + steps2[key]
        if steps < min_steps:
            min_steps = steps
    return min_steps


f = open('day3.txt')
p1 = f.readline().strip().split(',')
p2 = f.readline().strip().split(',')


def partOne():
    return solve(p1, p2)


def partTwo():
    return time_sensitive(p1, p2)


print('Part 1:', partOne())
print('Part 2:', partTwo())
