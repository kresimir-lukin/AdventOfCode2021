import sys

def hex_to_binary(hex):
    binary = []
    for digit in hex:
        bin_4digits = bin(int(digit, 16))[2:].zfill(4)
        binary.extend(bin_4digits)
    return ''.join(binary)

def get(transmission, position, length):
    position_end = position + length
    if position_end > len(transmission):
        return None, len(transmission)
    return transmission[position:position_end], position_end

def evaluate(packet_type, accumulator, value):
    if accumulator is None:
        return value
    if packet_type == '000':
        return accumulator + value
    if packet_type == '001':
        return accumulator * value
    if packet_type == '010':
        return min(accumulator, value)
    if packet_type == '011':
        return max(accumulator, value)
    if packet_type == '101':
        return int(accumulator > value)
    if packet_type == '110':
        return int(accumulator < value)
    if packet_type == '111':
        return int(accumulator == value)

def decode(transmission, position=0):
    version, position = get(transmission, position, 3)
    packet_type, position = get(transmission, position, 3)
    version_sum, value = int(version, 2), None
    if packet_type == '100':
        done, value = False, 0
        while not done:
            done = transmission[position] == '0'
            num, position = get(transmission, position, 5)
            value = value<<4 | int(num[1:], 2)
    else:
        length_type, position = get(transmission, position, 1)
        if length_type == '0':
            bits, position = get(transmission, position, 15)
            current, bits = position, int(bits, 2)
            while current + bits > position:
                inner_version_sum, inner_value, position = decode(transmission, position)
                version_sum += inner_version_sum
                value = evaluate(packet_type, value, inner_value)
        else:
            packets, position = get(transmission, position, 11)
            for _ in range(int(packets, 2)):
                inner_version_sum, inner_value, position = decode(transmission, position)
                version_sum += inner_version_sum
                value = evaluate(packet_type, value, inner_value)
    return version_sum, value, position

assert len(sys.argv) == 2
transmission = hex_to_binary(open(sys.argv[1]).read())

part1, part2, _ = decode(transmission)

print(f'Part 1: {part1}, Part 2: {part2}')