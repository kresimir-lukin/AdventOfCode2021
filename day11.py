import sys

def step(energy):
    flashes, stack = 0, []
    for r in range(10):
        for c in range(10):
            energy[r][c] += 1
            if energy[r][c] > 9:
                flashes += 1
                energy[r][c] = 0
                stack.append((r,c))
    while stack:
        r, c = stack.pop()
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 10 and 0 <= nc < 10 and energy[nr][nc] > 0:
                energy[nr][nc] += 1
                if energy[nr][nc] > 9:
                    flashes += 1
                    energy[nr][nc] = 0
                    stack.append((nr, nc))
    return flashes

def part1(energy):
    return sum(step(energy) for _ in range(100))

def part2(energy):
    steps = 0
    while sum(map(sum, energy)) > 0:
        step(energy)
        steps += 1
    return steps

assert len(sys.argv) == 2
energy = [list(map(int, row)) for row in open(sys.argv[1]).read().splitlines()]

print(f'Part 1: {part1([row[:] for row in energy])}, Part 2: {part2([row[:] for row in energy])}')