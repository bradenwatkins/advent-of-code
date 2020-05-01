from copy import deepcopy


class Intcode():
    def __init__(self, codes, noun=None, verb=None):
        self.i = 0
        self.MODE_POS = '0'
        self.CODE_EXIT = '99'
        self.codes = deepcopy(codes)
        self.codes[1] = noun if noun != None else self.codes[1]
        self.codes[2] = verb if verb != None else self.codes[2]
        self.commands = {
            '01': self.add,
            '02': self.mul,
            '03': self.input,
            '04': self.output,
            '05': self.jt,
            '06': self.jf,
            '07': self.lt,
            '08': self.eq
        }

    def opcode(self):
        cmd = str(self.codes[self.i]).zfill(2)
        return cmd[len(cmd)-2:len(cmd)]

    def unpack(self, count, dest=-1):
        res = list()
        modes = str(self.codes[self.i]).zfill(5)
        for i in range(1, count+1):
            a = self.codes[self.i+i]
            if i != dest:
                mode_i = modes[3-i]
                a = self.codes[a] if mode_i == self.MODE_POS else a
            res.append(a)
        return map(int, res) if len(res) > 1 else res[0]

    def add(self):
        a, b, c = self.unpack(3, dest=3)
        self.codes[c] = a + b
        self.i += 4

    def mul(self):
        a, b, c = self.unpack(3, dest=3)
        self.codes[c] = a * b
        self.i += 4

    def input(self):
        dest = self.unpack(1, dest=1)
        print("Input: ", end='')
        self.codes[dest] = int(input())
        self.i += 2

    def output(self):
        out = self.unpack(1)
        if out != 0:
            print('Output:', out)
        self.i += 2

    def jt(self):
        a, b = self.unpack(2)
        self.i = b if bool(a) else self.i + 3

    def jf(self):
        a, b = self.unpack(2)
        self.i = self.i+3 if bool(a) else b

    def lt(self):
        a, b, c = self.unpack(3, dest=3)
        self.codes[c] = 1 if a < b else 0
        self.i += 4

    def eq(self):
        a, b, c = self.unpack(3, dest=3)
        self.codes[c] = 1 if a == b else 0
        self.i += 4

    def run(self):
        next_code = self.opcode()
        while next_code != self.CODE_EXIT:
            if next_code not in self.commands:
                print("Unknown command found", next_code)
                return None
            self.commands[next_code]()
            next_code = self.opcode()
        return self.codes[0]


f = open('day5.txt')

f_codes = [int(line) for line in f.read().strip().split(',')]


def partOne():
    print('Part 1:')
    Intcode(f_codes).run()
    print()


def partTwo():
    print('Part 2:')
    Intcode(f_codes).run()


partOne()
partTwo()
