import sys, heapq

def calculate_min_risk(cavern):
    n, m = len(cavern), len(cavern[0])
    risks = [[-1]*m for _ in range(n)]
    risks[0][0] = 0
    q = [(0, 0, 0)]
    while risks[-1][-1] == -1:
        risk, r, c = heapq.heappop(q)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and risks[nr][nc] == -1:
                risks[nr][nc] = risk + cavern[nr][nc]
                heapq.heappush(q, (risks[nr][nc], nr, nc))
    return risks[-1][-1]

def build_5x_cavern(cavern):
    n, m = len(cavern), len(cavern[0])
    new_cavern = [[0] * (5 * m) for _ in range(5 * n)]
    for row in range(5):
        for col in range(5):
            for r in range(n):
                for c in range(m):
                    nr, nc = n * row + r, m * col + c
                    new_cavern[nr][nc] = cavern[r][c] + row + col
                    if new_cavern[nr][nc] > 9:
                        new_cavern[nr][nc] -= 9
    return new_cavern

assert len(sys.argv) == 2
cavern = [list(map(int, list(line))) for line in open(sys.argv[1]).read().splitlines()]

part1 = calculate_min_risk(cavern)
part2 = calculate_min_risk(build_5x_cavern(cavern))

print(f'Part 1: {part1}, Part 2: {part2}')