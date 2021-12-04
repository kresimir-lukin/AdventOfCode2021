import sys

def play_bingo_get_winning_scores(numbers, boards):
    number_board = {}
    board_totals = {}
    rows_pending = {}
    cols_pending = {}

    for board_index, board in enumerate(boards):
        for row_index, row in enumerate(board):
            for col_index, number in enumerate(row):
                if number not in number_board:
                    number_board[number] = set()
                number_board[number].add((board_index, row_index, col_index))
                board_totals[board_index] = board_totals.get(board_index, 0) + number
                rows_pending[board_index] = [5] * 5
                cols_pending[board_index] = [5] * 5

    done = [False] * len(boards)
    winning_scores = []

    for number in numbers:
        for board_index, row_index, col_index in number_board.get(number, []):
            board_totals[board_index] -= number
            rows_pending[board_index][row_index] -= 1
            cols_pending[board_index][col_index] -= 1
            if not done[board_index] and (rows_pending[board_index][row_index] == 0 or cols_pending[board_index][col_index] == 0):
                done[board_index] = True
                winning_scores.append(number * board_totals[board_index])

    return winning_scores

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()

numbers = list(map(int, lines[0].split(',')))
boards = []
for board_start_index in range(2, len(lines), 6):
    boards.append([])
    for board_index in range(board_start_index, board_start_index + 5):
        row = list(map(int, lines[board_index].split()))
        boards[-1].append(row)

winning_scores = play_bingo_get_winning_scores(numbers, boards)
part1, part2 = winning_scores[0], winning_scores[-1]

print(f'Part 1: {part1}, Part 2: {part2}')