def part1(raw_data):
    total = 0
    lines = [x.split(' ') for x in raw_data.split('\n')]
    for line in lines:
        counts = list(map(int, line[0].split('-')))
        letter = line[1][:-1]
        password = line[2]
        actual_count = password.count(letter)
        if counts[0] <= actual_count and actual_count <= counts[1]:
            total += 1
    return total


def part2(raw_data):
    total = 0
    lines = [x.split(' ') for x in raw_data.split('\n')]
    for line in lines:
        indices = [int(line) - 1 for line in line[0].split('-')]
        letter = line[1][:-1]
        password = line[2]
        if sum([password[indices[0]] == letter, password[indices[1]] == letter]) == 1:
            total += 1
    return total
