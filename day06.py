import sys

def count_lanternfish(lanternfish, days):
    cycle_counts = [0] * 9
    for cycle in lanternfish:
        cycle_counts[cycle] += 1
    for _ in range(days):
        new_cycle_counts = [cycle_counts[cycle] for cycle in range(1, 9)] + [cycle_counts[0]]
        new_cycle_counts[6] += cycle_counts[0]
        cycle_counts = new_cycle_counts
    return sum(cycle_counts)

assert len(sys.argv) == 2
lanternfish = list(map(int, open(sys.argv[1]).read().split(',')))

print(f'Part 1: {count_lanternfish(lanternfish, 80)}, Part 2: {count_lanternfish(lanternfish, 256)}')