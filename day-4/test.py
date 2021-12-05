import unittest
from typing import List
from bingo import Bingo
import bingo_board

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_bingo_sample(self) -> None:
        lines = file_read_helper('day-4/sample_input.txt')
        bingo = Bingo(lines)
        winning_score = bingo.play_bingo()
        self.assertEqual(winning_score, 4512)

    def test_bingo_puzzle(self) -> None:
        lines = file_read_helper('day-4/puzzle_input.txt')
        bingo = Bingo(lines)
        winning_score = bingo.play_bingo()
        self.assertEqual(winning_score, 63552)

    def test_lose_bingo_sample(self) -> None:
        lines = file_read_helper('day-4/sample_input.txt')
        bingo = Bingo(lines)
        losing_score = bingo.play_bingo_to_lose()
        self.assertEqual(losing_score, 1924)

    def test_lose_bingo_puzzle(self) -> None:
        lines = file_read_helper('day-4/puzzle_input.txt')
        bingo = Bingo(lines)
        losing_score = bingo.play_bingo_to_lose()
        self.assertEqual(losing_score, 9020)



class TestBingoBoard(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_is_bingo_is_false_with_no_bingo(self) -> None:
        board = bingo_board.BingoBoard()
        board.parse_input(["1 2 3 4 5", "1 2 3 4 5", "1 2 3 4 5", "1 2 3 4 5", "1 2 3 4 5"])
        board.mark_number(26)
        self.assertFalse(board.is_bingo())

    def test_is_bingo_is_true_with_row_bingo(self) -> None:
        board = bingo_board.BingoBoard()
        board.parse_input(["1 2 3 4 5", "1 2 3 4 5", "1 2 3 4 5", "26 26 26 26 26", "1 2 3 4 5"])
        board.mark_number(26)
        self.assertTrue(board.is_bingo())

    def test_is_bingo_is_true_with_col_bingo(self) -> None:
        board = bingo_board.BingoBoard()
        board.parse_input(["1 2 3 26 5", "1 2 3 26 5", "1 2 3 26 5", "1 2 3 26 5", "1 2 3 26 5"])
        board.mark_number(26)
        self.assertTrue(board.is_bingo())

    def test_sum_unmarked(self) -> None:
        board = bingo_board.BingoBoard()
        board.parse_input(["1 26 26 26 26", "26 2 26 26 26", "26 26 3 26 26", "26 26 26 4 26", "26 26 26 26 5"])
        board.mark_number(26)
        self.assertEqual(board.sum_unmarked(), 15)

def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
