def squash(signal, cache, start):
    end = len(signal)
    ssum = sum([s for s in signal[start:]])
    for i in range(start, end):
        cache[i] = ssum % 10
        ssum -= signal[i]

    return cache, signal


def long_transform(signal, n, start=0):
    cache = [0]*len(signal)
    for _ in range(n):
        signal, cache = squash(signal, cache, start)
    return map(str, signal)


def transform(signal, n):
    pattern = [0, 1, 0, -1]
    for _ in range(n):
        nextSignal = list()
        for i in range(len(signal)):
            res = sum([s*pattern[(j+1) // (i+1) % 4]
                       for j, s in enumerate(signal)])
            nextSignal.append(abs(res) % 10)
        signal = nextSignal
    return map(str, signal)


f = open('day16.txt')
f_signal = list(map(int, list(f.read().strip())))


def partOne():
    return ''.join(transform(list(f_signal), 100))[:8]


def partTwo():
    signal = list()
    for _ in range(10000):
        signal += f_signal
    offset = int(''.join(map(str, signal[:7])))
    return ''.join(long_transform(signal, 100, start=offset))[offset:offset+8]


print('Part 1:', partOne())
print('Part 2:', partTwo())
