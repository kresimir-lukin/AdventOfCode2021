import sys

def add(value, increment, modulo):
    return (value + increment - 1) % modulo + 1

def part1(player1, player2):
    positions = [player1, player2]
    scores = [0, 0]
    turn, rolled, dice = 0, 0, 1
    while max(scores) < 1000:
        for _ in range(3):
            positions[turn] = add(positions[turn], dice, 10)
            dice = add(dice, 1, 100)
        scores[turn] += positions[turn]
        rolled += 3
        turn = 1 - turn
    return min(scores) * rolled

def part2(player1, player2):
    def _roll_quantum_die(player_state):
        quantum_outcomes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
        new_state = {}
        for (position, score), frequency in player_state.items():
            for outcome_value, outcome_frequency in quantum_outcomes.items():
                new_position = add(position, outcome_value, 10)
                key = (new_position, score + new_position)
                new_state[key] = new_state.get(key, 0) + frequency * outcome_frequency
        return new_state
    def _prune_win_states(player1, player2):
        wins = 0
        for key in list(player1.keys()):
            if key[1] >= 21:
                wins += player1[key] * sum(player2.values())
                del player1[key]
        return wins
    player1 = {(player1, 0): 1}
    player2 = {(player2, 0): 1}
    player1_wins = 0
    while player1 and player2:
        player1 = _roll_quantum_die(player1)
        player1_wins += _prune_win_states(player1, player2)
        player2 = _roll_quantum_die(player2)
        _prune_win_states(player2, player1)
    return player1_wins

assert len(sys.argv) == 2
input_data = open(sys.argv[1]).read().splitlines()
player1 = int(input_data[0].split()[-1])
player2 = int(input_data[1].split()[-1])

print(f'Part 1: {part1(player1, player2)}, Part 2: {part2(player1, player2)}')