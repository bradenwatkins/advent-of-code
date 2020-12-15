def check_slope(lines, right, down):
    trees, x, y = 0, 0, 0
    while y < len(lines):
        if lines[y][x] == "#":
            trees += 1
        x = (x + right) % len(lines[y])
        y = y + down
    return trees

def part1(raw_data):
    lines = [x for x in raw_data.split('\n')]
    return check_slope(lines, 3, 1)


def part2(raw_data):
    lines = [x for x in raw_data.split('\n')]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for slope in slopes:
        product *= check_slope(lines, slope[0], slope[1])
    return product
