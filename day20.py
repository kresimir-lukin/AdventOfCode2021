import sys

def count_lights(image):
    return sum(sum(row) for row in image)

def enhance(image, algorithm, times):
    rows, cols = len(image), len(image[0])
    def _enhance(image, default):
        image_enhanced = [[default] * cols for _ in range(rows)]
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                index = ''.join(str(image[r + dr][c + dc]) for dr in range(-1, 2) for dc in range(-1, 2))
                image_enhanced[r][c] = algorithm[int(index, 2)]
        return image_enhanced
    for _ in range(times // 2):
        image = _enhance(image, algorithm[0])
        image = _enhance(image, 0)
    return image

assert len(sys.argv) == 2
input_data = open(sys.argv[1]).read().splitlines()
algorithm = [int(pixel == '#') for pixel in input_data[0]]
rows, cols = len(input_data)-2, len(input_data[2])
image = [[0] * (cols + 102) for _ in range(rows + 102)]

for r in range(rows):
    for c in range(cols):
        image[r + 51][c + 51] = int(input_data[r + 2][c] == '#')

part1 = count_lights(enhance(image, algorithm, 2))
part2 = count_lights(enhance(image, algorithm, 50))

print(f'Part 1: {part1}, Part 2: {part2}')