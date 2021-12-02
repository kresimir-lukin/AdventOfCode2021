import sys

def part1(commands):
    x = y = 0
    for direction, number in commands:
        if direction == 'forward':
            x += number
        else:
            y += number if direction == 'down' else -number
    return x * y

def part2(commands):
    x = y = aim = 0
    for direction, number in commands:
        if direction == 'forward':
            x += number
            y += aim * number
        else:
            aim += number if direction == 'down' else -number
    return x * y

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()
commands = [(line.split()[0], int(line.split()[1])) for line in lines]

print(f'Part 1: {part1(commands)}, Part 2: {part2(commands)}')