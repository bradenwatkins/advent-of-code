def find_weakness(nums):
    for i in range(25, len(nums)):
        target = nums[i]
        pool = set(nums[i-25:i])
        if not any([target - a in pool for a in pool]):
            return target

def part1(raw_data):
    nums = list(map(int, raw_data.split("\n")))
    return find_weakness(nums)

def part2(raw_data):
    nums = list(map(int, raw_data.split("\n")))
    weakness = find_weakness(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            window = nums[i:j]
            total = sum(window)
            if total < weakness:
                continue
            if total == weakness:
                return min(window) + max(window)