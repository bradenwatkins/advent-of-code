from collections import deque

def count_bags(bags, source):
    queue = deque([source])
    count = -1
    while queue:
        count += 1
        queue.extend(bags[queue.popleft()])
    return count

def can_carry(bags, source, target):
    queue = deque([source])
    while queue:
        dest = set(bags[queue.popleft()])
        if target in dest: return True
        queue.extend(dest)
    return False

def to_graph(rules):
    bags = dict()
    for rule in rules:
        rule = rule.replace(".", "")                        # remove period
        rule = rule.replace("bags", "")                     # remove bags
        rule = rule.replace("bag", "")                      # remove bag
        src, dst = rule.split("contain")                    # split on contain
        src = src.strip()                                   # strip whitespace
        bags[src] = list()
        for d in dst.split(","):                            # split on ,
            if "no other" not in d:                         # ignore bags that contain "no other"
                d = d.strip()
                count, bag = int(d[0]), d[2:]               # separate count from name
                bags[src] += [bag] * count             
    return bags


def part1(raw_data):
    rules = [x for x in raw_data.split('\n')]
    bags = to_graph(rules)
    return sum([can_carry(bags, source, "shiny gold") for source in bags])

def part2(raw_data):
    rules = [x for x in raw_data.split('\n')]
    bags = to_graph(rules)
    return count_bags(bags, "shiny gold")