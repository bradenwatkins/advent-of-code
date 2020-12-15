def any_yes(group):
    return len(set().union(*[set(person) for person in group]))

def part1(raw_data):
    groups = [x.split('\n') for x in raw_data.split('\n\n')]
    return sum([any_yes(g) for g in groups])

def all_yes(group):
    return len(set(group[0]).intersection(*[set(person) for person in group]))

def part2(raw_data):
    groups = [x.split('\n') for x in raw_data.split('\n\n')]
    return sum([all_yes(g) for g in groups])