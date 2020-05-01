from copy import deepcopy


class Intcode():
    def __init__(self, codes, noun, verb):
        self.i = 0
        self.codes = deepcopy(codes)
        self.codes[1] = noun
        self.codes[2] = verb
        self.commands = {
            1: self.add,
            2: self.mul,
        }

    def add(self):
        a, b, dest = map(int, self.codes[self.i+1:self.i+4])
        self.codes[dest] = self.codes[a] + self.codes[b]
        return 4

    def mul(self):
        a, b, dest = map(int, self.codes[self.i+1:self.i+4])
        self.codes[dest] = self.codes[a] * self.codes[b]
        return 4

    def run(self):
        while self.codes[self.i] != 99:
            command = self.codes[self.i]
            if command not in self.commands:
                print("Unknown command found", command)
                return None
            self.i += self.commands[self.codes[self.i]]()
        return self.codes[0]


def find(codes, target, max_range=100):
    for noun in range(max_range):
        for verb in range(max_range):
            if Intcode(codes, noun, verb).run() == target:
                return 100 * noun + verb
    return 'Not found'


f = open('day2.txt')

f_codes = [int(line) for line in f.read().strip().split(',')]


def partOne():
    return Intcode(f_codes, 12, 1).run()


def partTwo():
    return find(f_codes, 19690720)


print('Part 1:', partOne())
print('Part 2:', partTwo())
