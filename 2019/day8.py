import math


def get_layers(image, width, height):
    layers = list()
    currentLayer = list()
    currentRow = list()
    for i in range(len(image)):
        currentRow.append(image[i])
        if (i+1) % width == 0:
            currentLayer.append(currentRow)
            currentRow = list()
        if (i+1) % (width * height) == 0:
            layers.append(currentLayer)
            currentLayer = list()
    return layers


def get_min_zero_layer(layers):
    min_count = math.inf
    result = None
    for layer in layers:
        zeros = sum([x.count('0') for x in layer])
        if zeros < min_count:
            result = layer
            min_count = zeros
    return result


def zip_layers(layers, width, height):
    result = [['2' for y in range(width)] for x in range(height)]
    for layer in layers:
        for i, row in enumerate(layer):
            for j, val in enumerate(row):
                if result[i][j] == '2' and val != '2':
                    result[i][j] = val
    return result


f = open('day8.txt')
width, height = map(int, f.readline().strip().split(' '))
image = f.readline().strip()


def partOne():
    layers = get_layers(image, width, height)
    max_zero_layer = get_min_zero_layer(layers)
    ones = sum([x.count('1') for x in max_zero_layer])
    twos = sum([x.count('2') for x in max_zero_layer])
    return ones * twos


def partTwo():
    layers = get_layers(image, width, height)
    zipped = zip_layers(layers, width, height)
    result = '\n'
    for row in zipped:
        result += ''.join(row).replace('0', ' ') + '\n'
    return result


print('Part 1:', partOne())
print('Part 2:', partTwo())
