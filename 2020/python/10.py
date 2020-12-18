def part1(raw_data):
    adaptors = list(map(int, raw_data.split("\n")))
    adaptors.sort()
    jolts, ones, threes = 0, 0, 0
    for a in adaptors:
        ones += 1 if a - jolts == 1 else 0
        threes += 1 if a - jolts == 3 else 0
        jolts = a
    threes += 1
    return ones * threes

def part2(raw_data):
    adaptors = list(map(int, raw_data.split("\n"))) + [0]
    adaptors.sort()
    adaptors.append(max(adaptors) + 3)
    counts = [0] * len(adaptors)
    counts[0] = 1
    for i, a in enumerate(adaptors):
      if i >= 3 and adaptors[i] - adaptors[i-3] <= 3:
        counts[i] += counts[i-3]
      if i >= 2 and adaptors[i] - adaptors[i-2] <= 3:
        counts[i] += counts[i-2]
      if i >= 1 and adaptors[i] - adaptors[i-1] <= 3:
        counts[i] += counts[i-1]
    return counts[-1]