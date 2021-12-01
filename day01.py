import sys

def count_depth_increases(depths, window):
    return sum(depths[i] < depths[i+window] for i in range(len(depths)-window))

assert len(sys.argv) == 2
depths = list(map(int, open(sys.argv[1]).read().split()))

print(f'Part 1: {count_depth_increases(depths, 1)}, Part 2: {count_depth_increases(depths, 3)}')