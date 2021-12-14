import sys
from collections import Counter

def polymerize(template, rules, steps):
    pair_frequencies = Counter()
    char_frequencies = Counter(template)
    
    for pos in range(1, len(template)):
        pair = template[pos-1:pos+1]
        pair_frequencies[pair] += 1

    for _ in range(steps):
        pair_frequencies_step = Counter()
        for pair, frequency in pair_frequencies.items():
            if pair in rules:
                pair_frequencies_step[pair[0] + rules[pair]] += frequency
                pair_frequencies_step[rules[pair] + pair[1]] += frequency
                char_frequencies[rules[pair]] += frequency
        pair_frequencies = pair_frequencies_step

    return max(char_frequencies.values()) - min(char_frequencies.values())

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()

template = lines[0]
rules = {left: right for left, right in (line.split(' -> ') for line in lines[2:])}

part1 = polymerize(template, rules, 10)
part2 = polymerize(template, rules, 40)

print(f'Part 1: {part1}, Part 2: {part2}')