def find_two(arr):
  entry_set = set(arr)
  for x in entry_set:
    if 2020 - x in entry_set:
      return x * (2020-x)

def find_three(arr):
  entry_set = set(arr)
  for i, x in enumerate(arr):
    for y in enumerate(arr[i:]):
      if 2020 - x - y in entry_set:
        return x * y * (2020 - x - y)

f = open('day1.txt')
entries = [int(line) for line in f.read().strip().split('\n')]


def partOne():
    return find_two(entries)


def partTwo():
    return find_three(entries)


print('Part 1:', partOne())
print('Part 2:', partTwo())
