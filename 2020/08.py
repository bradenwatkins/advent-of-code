NOP = 'nop'
ACC = 'acc'
JMP = 'jmp'


class Handheld:
    def __init__(self):
        self.ops = {
            NOP: self.exec_nop,
            ACC: self.exec_acc,
            JMP: self.exec_jmp
        }
        self.swap = {
            NOP: JMP,
            ACC: ACC,
            JMP: NOP
        }

    def safe_run(self, instructions, swap = None):
        ran = set()
        self.ptr, self.acc = 0, 0
        while self.ptr not in ran and self.ptr < len(instructions):
            ran.add(self.ptr) 
            op, arg = self.parse_instruction(instructions[self.ptr])
            if swap != None and self.ptr == swap:
                op = self.swap[op]
            self.ops[op](arg)
        return self.ptr == len(instructions)
            
    def parse_instruction(self, instruction):
        op, arg = instruction.split(" ")
        return op, int(arg)

    def exec_nop(self, arg):
        self.ptr += 1

    def exec_acc(self, arg):
        self.acc += arg
        self.ptr += 1

    def exec_jmp(self, arg):
        self.ptr += arg

def part1(raw_data):
    instructions = [x for x in raw_data.split('\n')]
    handheld = Handheld()
    handheld.safe_run(instructions)
    return handheld.acc

def part2(raw_data):
    instructions = [x for x in raw_data.split('\n')]
    handheld = Handheld()
    for i in range(len(instructions)):
        if handheld.safe_run(instructions, swap=i):
            return handheld.acc