from typing import List

MARKED = 'X'

class BingoBoard:
    def __init__(self) -> None:
        self.board = [[None for _ in range(5)] for _ in range(5)]

    def __str__(self) -> str:
        return str(self.board)

    def parse_input(self, input_lines: List[str]) -> None:
        for i, line in enumerate(input_lines):
            for j, number_str in enumerate(line.split()):
                self.board[i][j] = int(number_str, 10)

    def mark_number(self, number: int) -> None:
        for row in self.board:
            for i, cell in enumerate(row):
                if cell == number:
                    row[i] = MARKED

    def is_bingo(self) -> bool:
        for i in range(5):
            if self.board[i] == [MARKED] * 5:
                return True
            if [row[i] for row in self.board] == [MARKED] * 5:
                return True
        return False

    def sum_unmarked(self) -> int:
        return sum(sum(0 if cell == MARKED else cell for cell in row) for row in self.board)