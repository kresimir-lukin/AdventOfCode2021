import sys, math

def multiplier(c):
    return 10**('ABCD'.index(c))

def move(row, i, rooms, roomid, j):
    rooms = rooms[:]
    if row[i] == '.':
        row = row[:i] + rooms[roomid][j] + row[i+1:]
        rooms[roomid] = rooms[roomid][:j] + '.' + rooms[roomid][j+1:]
    else:
        rooms[roomid] = rooms[roomid][:j] + row[i] + rooms[roomid][j+1:]
        row = row[:i] + '.' + row[i+1:]
    return row, rooms

def room_position(roomid):
    return [2, 4, 6, 8][roomid]

def get_left_right(row, roomid, c):
    left = next((i for i in range(room_position(roomid), -1, -1) if row[i] not in '.#'), -1)
    right = next((i for i in range(room_position(roomid), len(row)) if row[i] not in '.#'), -1)
    return [i for i in (left, right) if i != -1 and row[i] == c]

def get_available_left_right(row, roomid):
    left = right = room_position(roomid)
    while left >= 0 and row[left] in '.#':
        left -= 1
    while right < len(row) and row[right] in '.#':
        right += 1
    return [i for i in range(left+1, right) if row[i] == '.']

def least_energy(rooms):
    observed_states = {}
    def _least_energy(row, rooms):
        if all(room.count(c) == len(room) for c, room in zip('ABCD', rooms)):
            return 0
        state = (row, tuple(rooms))
        if state in observed_states:
            return observed_states[state]
        result = math.inf
        for roomid, c in enumerate('ABCD'):
            if rooms[roomid].replace('.', c) == c * len(rooms[roomid]):
                position = rooms[roomid].count('.')
                for i in get_left_right(row, roomid, c):
                    cost = multiplier(c) * (position + abs(room_position(roomid) - i))
                    result = min(result, cost + _least_energy(*move(row, i, rooms, roomid, position-1)))
            elif rooms[roomid].count(c) != len(rooms[roomid]):
                position = rooms[roomid].count('.')
                for i in get_available_left_right(row, roomid):
                    cost = multiplier(rooms[roomid][position]) * (position + 1 + abs(room_position(roomid) - i))
                    result = min(result, cost + _least_energy(*move(row, i, rooms, roomid, position)))
        observed_states[state] = result
        return result
    return _least_energy('..#.#.#.#..', rooms)

assert len(sys.argv) == 2
puzzle = open(sys.argv[1]).read().splitlines()
rooms = [puzzle[2][i] + puzzle[3][i] for i in range(3, 10, 2)]

part1 = least_energy(rooms)
part2 = least_energy([room[0] + addition + room[1] for room, addition in zip(rooms, ['DD', 'CB', 'BA', 'AC'])])

print(f'Part 1: {part1}, Part 2: {part2}')