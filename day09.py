import sys

def part1(height_map):
    rows, cols = len(height_map), len(height_map[0])
    sum_lowest = 0
    for r in range(rows):
        for c in range(cols):
            min_neighbour = min(height_map[r+dr][c+dc] for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= r+dr < rows and 0 <= c+dc < cols)
            if height_map[r][c] < min_neighbour:
                sum_lowest += int(height_map[r][c]) + 1
    return sum_lowest

def part2(height_map):
    rows, cols = len(height_map), len(height_map[0])
    visited = [[False]*cols for _ in range(rows)]
    def _visit_dfs(r, c):
        size, visited[r][c] = 1, True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and height_map[nr][nc] != '9' and not visited[nr][nc]:
                size += _visit_dfs(nr, nc)
        return size
    basins = []
    for r in range(rows):
        for c in range(cols):
            if height_map[r][c] != '9' and not visited[r][c]:
                basins.append(_visit_dfs(r, c))
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]

assert len(sys.argv) == 2
height_map = open(sys.argv[1]).read().splitlines()

print(f'Part 1: {part1(height_map)}, Part 2: {part2(height_map)}')