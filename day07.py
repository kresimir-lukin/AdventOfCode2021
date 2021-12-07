import sys

def arithmetic_sum(n):
    return n * (n + 1) // 2

def fuel_to_optimal_position(positions, cost_fn):
    minimum_fuel = float('inf')
    # try every position between range to keep it simple, it can be done more efficiently with binary search since fuel to position is convex function
    for position in range(min(positions), max(positions) + 1):
        fuel_to_position = sum(map(lambda p: cost_fn(position, p), positions))
        minimum_fuel = min(minimum_fuel, fuel_to_position)
    return minimum_fuel

assert len(sys.argv) == 2
positions = list(map(int, open(sys.argv[1]).read().split(',')))

part1 = fuel_to_optimal_position(positions, lambda p1, p2: abs(p1 - p2))
part2 = fuel_to_optimal_position(positions, lambda p1, p2: arithmetic_sum(abs(p1 - p2)))

print(f'Part 1: {part1}, Part 2: {part2}')