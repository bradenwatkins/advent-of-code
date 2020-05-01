class Generator():
    def __init__(self, reactions):
        self.reactions = dict()
        for r in reactions:
            x, y = r.split('=>')
            y = y.strip().split(' ')
            count = int(y[0])
            result = y[1]
            self.reactions[result] = dict()
            self.reactions[result]['count'] = count
            self.reactions[result]['ingredients'] = dict()
            for i in x.strip().split(','):
                i = i.strip().split(' ')
                count = int(i[0])
                ingredient = i[1]
                self.reactions[result]['ingredients'][ingredient] = count

    def generate(self, type, count):
        if type == 'ORE':
            return count
        generated = 0
        fuel_needed = 0
        while generated < count:
            generated += self.reactions[type]['count']
            fuel_needed += sum([self.generate(t, c)
                                for t, c in self.reactions[type]['ingredients'].items()])
        return fuel_needed


f = open('day14.txt')
reactions = f.read().strip().split('\n')


def partOne():
    g = Generator(reactions)
    return g.generate('FUEL', 1)


def partTwo():
    pass


print('Part 1:', partOne())
print('Part 2:', partTwo())
