import sys

def get_digits_by_length(digits, length):
    return [''.join(sorted(digit)) for digit in digits if len(digit) == length]

def get_digit_mapping(digits):
    digits2 = get_digits_by_length(digits, 2)
    digits3 = get_digits_by_length(digits, 3)
    digits4 = get_digits_by_length(digits, 4)
    digits5 = get_digits_by_length(digits, 5)
    digits6 = get_digits_by_length(digits, 6)
    digits7 = get_digits_by_length(digits, 7)

    mapping = {
        digits2[0]: '1',
        digits4[0]: '4',
        digits3[0]: '7',
        digits7[0]: '8'
    }

    d3 = next(digit for digit in digits5 if len(set(digit) - set(digits3[0])) == 2)
    mapping[d3] = '3'
    digits5.remove(d3)

    d6 = next(digit for digit in digits6 if set(digits3[0]) - set(digit))
    mapping[d6] = '6'
    digits6.remove(d6)

    d5, d9 = next((d5, d6) for d6 in digits6 for d5 in digits5 if len(set(d6) & set(d5)) == 5)
    mapping[d5] = '5'
    mapping[d9] = '9'
    digits5.remove(d5)
    digits6.remove(d9)

    mapping[digits5.pop()] = '2' 
    mapping[digits6.pop()] = '0'

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