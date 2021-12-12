import sys

def build_graph(edges):
    graph = {}
    for cave1, cave2 in edges:
        if cave1 not in graph:
            graph[cave1] = set()
        if cave2 not in graph:
            graph[cave2] = set()
        graph[cave1].add(cave2)
        graph[cave2].add(cave1)
    return graph

def count_paths(graph, double_pass_used, node='start', seen=['start']):
    if node == 'end':
        return 1
    count = 0
    for neighbour in graph[node]:
        if neighbour != 'start':
            if neighbour[0].isupper() or neighbour not in seen:
                count += count_paths(graph, double_pass_used, neighbour, seen + [neighbour])
            elif not double_pass_used:
                count += count_paths(graph, True, neighbour, seen)
    return count

assert len(sys.argv) == 2
edges = list(map(lambda x: x.split('-'), open(sys.argv[1]).read().splitlines()))

graph = build_graph(edges)
part1 = count_paths(graph, True)
part2 = count_paths(graph, False)

print(f'Part 1: {part1}, Part 2: {part2}')