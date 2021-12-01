import sys

def count_depth_increases(depths, window):
    return sum(sum(depths[i-1:i+window-1]) < sum(depths[i:i+window]) for i in range(1, len(depths)-window+1))

assert len(sys.argv) == 2
depths = list(map(int, open(sys.argv[1]).read().split()))

print(f'Part 1: {count_depth_increases(depths, 1)}, Part 2: {count_depth_increases(depths, 3)}')