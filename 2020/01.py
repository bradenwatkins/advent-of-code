def parse(raw_data):
  return [int(x) for x in raw_data.split('\n')]

def part1(raw_data):
  data = parse(raw_data)
  entry_set = set(data)
  for x in entry_set:
    if 2020 - x in entry_set:
      return x * (2020-x)

def part2(raw_data):
  data = parse(raw_data)
  entry_set = set(data)
  for i, x in enumerate(data):
    for y in data[i:]:
      if 2020 - x - y in entry_set:
        return x * y * (2020 - x - y)
