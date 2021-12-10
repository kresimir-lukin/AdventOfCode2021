import sys

def process_chunk(chunk):
    match = { ')': '(', ']': '[', '}': '{', '>': '<' }
    stack = []
    for ch in chunk:
        if ch in match:
            if match[ch] != stack.pop():
                return False, ch
        else:
            stack.append(ch)
    return True, stack

def part1(navigation):
    points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    score = 0
    for chunk in navigation:
        valid, invalid_ch = process_chunk(chunk)
        if not valid:
            score += points[invalid_ch]
    return score

def part2(navigation):
    points = { '(': 1, '[': 2, '{': 3, '<': 4 }
    scores = []
    for chunk in navigation:
        valid, remaining = process_chunk(chunk)
        if valid:
            scores.append(0)
            while remaining:
                scores[-1] = scores[-1] * 5 + points[remaining.pop()]
    return sorted(scores)[len(scores)//2]

assert len(sys.argv) == 2
navigation = open(sys.argv[1]).read().splitlines()

print(f'Part 1: {part1(navigation)}, Part 2: {part2(navigation)}')