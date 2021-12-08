import sys

def get_digits_by_length(digits, length):
    return [''.join(sorted(digit)) for digit in digits if len(digit) == length]

def get_digit_mapping(digits):
    segments2 = get_digits_by_length(digits, 2)
    segments3 = get_digits_by_length(digits, 3)
    segments4 = get_digits_by_length(digits, 4)
    segments5 = get_digits_by_length(digits, 5)
    segments6 = get_digits_by_length(digits, 6)
    segments7 = get_digits_by_length(digits, 7)

    mapping = {
        segments2[0]: '1',
        segments4[0]: '4',
        segments3[0]: '7',
        segments7[0]: '8'
    }

    # 3 is the only digit of 5 segments which contains all segments as 7, so diff must be 2
    d3 = next(digit for digit in segments5 if len(set(digit) - set(segments3[0])) == 2)
    mapping[d3] = '3'
    segments5.remove(d3)

    # 6 is the only digit of 6 segments which does not have all 3 segments as 7, so there must be diff of 1
    d6 = next(digit for digit in segments6 if len(set(segments3[0]) - set(digit)) == 1)
    mapping[d6] = '6'
    segments6.remove(d6)

    # 9 have all of the same segments as 5 plus 1 more, so diff of intersection must be 5
    d5, d9 = next((d5, d6) for d6 in segments6 for d5 in segments5 if len(set(d6) & set(d5)) == 5)
    mapping[d5] = '5'
    mapping[d9] = '9'
    segments5.remove(d5)
    segments6.remove(d9)

    # remaining numbers of 5 and 6 segments
    mapping[segments5.pop()] = '2' 
    mapping[segments6.pop()] = '0'

    return mapping

def part1(notes):
    count1478 = 0
    for _, output in notes:
        count1478 += sum(len(digit) in (2, 3, 4, 7) for digit in output.split())
    return count1478

def part2(notes):
    output_sum = 0
    for digits, output in notes:
        mapping = get_digit_mapping(digits.split())
        number = ''.join(mapping[''.join(sorted(digit))] for digit in output.split())
        output_sum += int(number)
    return output_sum

assert len(sys.argv) == 2
notes = list(map(lambda x: x.split(' | '), open(sys.argv[1]).read().splitlines()))

print(f'Part 1: {part1(notes)}, Part 2: {part2(notes)}')