import sys

def fold(coordinates, folds):
    for direction, number in folds:
        coordinates_folded = set()
        for x, y in coordinates:
            if direction == 'x':
                coordinates_folded.add((x if x < number else 2 * number - x, y))
            else:
                coordinates_folded.add((x, y if y < number else 2 * number - y))
        coordinates = coordinates_folded
    return coordinates

def part1(coordinates, folds):
    return len(fold(coordinates, folds[:1]))

def part2(coordinates, folds):
    folded_coordinates = fold(coordinates, folds)
    
    max_x = max(x for x, _ in folded_coordinates)
    max_y = max(y for _, y in folded_coordinates)
    display = [[' '] * (max_x + 1) for _ in range(max_y + 1)]
    
    for x, y in folded_coordinates:
        display[y][x] = '#'

    return '\n'.join(''.join(row) for row in display)

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()

coordinates, folds = set(), []
for line in lines:
    if ',' in line:
        x, y = map(int, line.split(','))
        coordinates.add((x, y))
    if line.startswith('fold'):
        direction, number = line.split()[-1].split('=')
        folds.append((direction, int(number)))

print(f'Part 1: {part1(coordinates, folds)}, Part 2: \n{part2(coordinates, folds)}')