import sys, copy

def magnitude(number):
    if isinstance(number, int):
        return number
    return 3 * magnitude(number[0]) + 2 * magnitude(number[1])

def add(x, y):
    snailfish = copy.deepcopy([x, y])
    while action(snailfish):
        pass
    return snailfish

def action(root):
    pair_left, i_left = None, None
    pair_right, i_right = None, None
    pair_split, i_split = None, None
    stack = [(0, [root, None], 0)]
    while stack:
        depth, pair, i = stack.pop()
        if isinstance(pair[i], int):
            if not pair_split and pair[i] >= 10:
                pair_split, i_split = pair, i
            pair_left, i_left = pair, i
        else:
            if depth >= 4:
                if stack:
                    _, pair_right, i_right = stack.pop()
                    while isinstance(pair_right[i_right], list):
                        pair_right, i_right = pair_right[i_right], 0
                if pair_left:
                    pair_left[i_left] += pair[i][0]
                if pair_right:
                    pair_right[i_right] += pair[i][1]
                pair[i] = 0
                return True
            else:
                stack.append((depth + 1, pair[i], 1))
                stack.append((depth + 1, pair[i], 0))
    if pair_split:
        pair_split[i_split] = [pair_split[i_split] // 2, (pair_split[i_split] + 1) // 2]
        return True
    return False

def part1(numbers):
    numbers = list(map(eval, numbers))
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = add(result, numbers[i])
    return magnitude(result)

def part2(numbers):
    numbers = list(map(eval, numbers))
    max_magnitude = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                addition = add(numbers[i], numbers[j])
                max_magnitude = max(max_magnitude, magnitude(addition))
    return max_magnitude

assert len(sys.argv) == 2
numbers = open(sys.argv[1]).read().splitlines()

print(f'Part 1: {part1(numbers)}, Part 2: {part2(numbers)}')