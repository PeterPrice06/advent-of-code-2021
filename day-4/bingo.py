from typing import List 
from bingo_board import BingoBoard

class Bingo():
    def __init__(self, lines: List[str]) -> None:
        self.drawn_numbers = []
        self.boards = []

        if lines != None:
            self.drawn_numbers = map(int, lines[0].split(','))
            for i in range(2, len(lines), 6):
                new_board = BingoBoard()
                new_board.parse_input(lines[i:i+5])
                self.boards.append(new_board)

    def __str__(self) -> str:
        formated_boards = [str(board) for board in self.boards]
        string = f'{self.drawn_numbers} \n'
        for board_str in formated_boards:
            string += f'{board_str} \n\n'
        return string
    
    def play_bingo(self) -> int:
        for number in self.drawn_numbers:
            for board in self.boards:
                board.mark_number(number)
                
                if board.is_bingo():
                    return board.sum_unmarked() * number
    
    def play_bingo_to_lose(self) -> int:
        number_of_boards = len(self.boards)
        marked_boards_for_removal = []
        for number in self.drawn_numbers:
            for i, board in enumerate(self.boards):
                if i in marked_boards_for_removal:
                    continue

                board.mark_number(number)
                if number_of_boards - len(marked_boards_for_removal) == 1 and board.is_bingo():
                    return board.sum_unmarked() * number

                if board.is_bingo():
                    marked_boards_for_removal.append(i)

                
 