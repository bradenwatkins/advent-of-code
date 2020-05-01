def parseOrbit(x):
    split = x.split(')')
    return split[0], split[1]


class OrbitGraph():
    def __init__(self, orbits):
        self.G = dict()
        self.R = dict()
        for a, b in map(parseOrbit, orbits):
            if a not in self.G:
                self.G[a] = set()
            self.G[a].add(b)
            self.R[b] = a

    def __checksum__(self, node):
        if node not in self.G:
            return 1, 0
        num_children = 0
        child_orbits = 0
        for child in self.G[node]:
            children, orbits = self.__checksum__(child)
            num_children += children
            child_orbits += orbits
        return 1 + num_children, num_children + child_orbits

    def checksum(self):
        _, orbits = self.__checksum__('COM')
        return orbits

    def get_rlen(self, node):
        l = 0
        while node != 'COM':
            l += 1
            node = self.R[node]
        return l

    def santa_dist(self):
        dist = 0
        you_node = 'YOU'
        san_node = 'SAN'
        you_len = self.get_rlen(you_node)
        san_len = self.get_rlen(san_node)
        while you_len > san_len:
            you_node = self.R[you_node]
            you_len -= 1
            dist += 1
        while san_len > you_len:
            san_node = self.R[san_node]
            san_len -= 1
            dist += 1
        while you_node != san_node:
            you_node = self.R[you_node]
            san_node = self.R[san_node]
            dist += 2
        dist -= 2
        return dist


f = open('day6.txt')
orbits = [line for line in f.read().strip().split('\n')]
G = OrbitGraph(orbits)


def partOne():
    return G.checksum()


def partTwo():
    return G.santa_dist()


print('Part 1:', partOne())
print('Part 2:', partTwo())
