import sys

def part1(report):
    gamma = epsilon = ''
    for bit in range(len(report[0])):
        s0 = sum(number[bit] == '0' for number in report)
        s1 = sum(number[bit] == '1' for number in report)
        gamma += '0' if s0 > s1 else '1'
        epsilon += '1' if s0 > s1 else '0'
    return int(gamma, 2) * int(epsilon, 2)

def part2(report):
    def _get_rating(fn_bit_criteria):
        numbers, bit = report[:], 0
        while len(numbers) > 1:
            n0 = [number for number in numbers if number[bit] == '0']
            n1 = [number for number in numbers if number[bit] == '1']
            numbers = fn_bit_criteria(n0, n1)
            bit += 1
        return int(numbers[0], 2)
    oxygen_generator = _get_rating(lambda n0, n1: n1 if len(n1) >= len(n0) else n0)
    co2_scrubber = _get_rating(lambda n0, n1: n0 if len(n1) >= len(n0) else n1)
    return oxygen_generator * co2_scrubber

assert len(sys.argv) == 2
report = open(sys.argv[1]).read().splitlines()

print(f'Part 1: {part1(report)}, Part 2: {part2(report)}')