import math


class RadialCounter():
    def __init__(self, radius):
        self.radius = 0
        self.lineset = set({(0, 1), (0, -1), (1, 0), (-1, 0)})
        for x in range(-radius, radius):
            for y in range(-radius, radius):
                if x == 0 or y == 0:
                    continue
                dx, dy = x, y
                for i in reversed(range(1, radius)):
                    if dx % i == 0 and dy % i == 0:
                        dx //= i
                        dy //= i
                self.lineset.add((dx, dy))
        self.lines = list(self.lineset)
        self.lines.sort(key=lambda line: math.atan2(
            line[0], -line[1]) % (math.pi*2))


def clear_sight(field, x, y, dx, dy):
    blocked = False
    y += dy
    x += dx
    while x >= 0 and y >= 0 and y < len(field) and x < len(field[y]):
        if field[y][x] == '#' and not blocked:
            blocked = True
        elif blocked:
            field[y][x] = '.'
        y += dy
        x += dx
    return field


def get_best(infield):
    max_count = -math.inf
    best = (-1, -1)
    for y in range(len(f_field)):
        for x in range(len(f_field[y])):
            if f_field[y][x] == '#':
                field = [list(line) for line in f_field]
                field[y][x] = 'X'
                radius = max(x, max(y, max(len(field)-y, len(field[y])-x)))
                radial = RadialCounter(radius)
                for dx, dy in radial.lines:
                    field = clear_sight(field, x, y, dx, dy)
                count = ''.join([''.join(line) for line in field]).count('#')
                if count > max_count:
                    best = (x, y)
                    max_count = count
    return max_count, best


def destroy(in_field):
    _, best = get_best([list(line) for line in in_field])
    field = [list(line) for line in f_field]
    count = 0
    order = list()
    x, y = best
    field[y][x] = 'X'
    total = ''.join([''.join(line) for line in field]).count('#')
    radius = max(x, max(y, max(len(field)-y, len(field[y])-x)))
    radial = RadialCounter(radius)
    while count < total:
        for dx, dy in radial.lines:
            x, y = best
            while x >= 0 and y >= 0 and y < len(field) and x < len(field[y]):
                if field[y][x] == '#':
                    field[y][x] = count + 1
                    order.append((x, y))
                    count += 1
                    break
                x += dx
                y += dy
    return order


f = open('day10.txt')
f_field = [list(line) for line in f.read().strip().split('\n')]


def partOne():
    max_count, _ = get_best([list(line) for line in f_field])
    return max_count


def partTwo():
    order = destroy([list(line) for line in f_field])
    fx, fy = order[199]
    return 100 * fx + fy


print('Part 1:', partOne())
print('Part 2:', partTwo())
