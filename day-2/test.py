import unittest
from typing import List
import solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = solution.Solution()

    def test_simple_calculate_naive_movement_position(self) -> None:
        moves = file_read_helper('simple_input.txt')
        horz, depth = self.solution.calculate_naive_movement_position(moves)
        self.assertEqual(horz, 15)
        self.assertEqual(depth, 10)

    def test_long_calculate_naive_movement_position(self) -> None:
        moves = file_read_helper('long_input.txt')
        horz, depth = self.solution.calculate_naive_movement_position(moves)
        self.assertEqual(horz, 1998)
        self.assertEqual(depth, 741)

    def test_simple_calculate_position(self) -> None:
        moves = file_read_helper('simple_input.txt')
        horz, depth = self.solution.calculate_position(moves)
        self.assertEqual(horz, 15)
        self.assertEqual(depth, 60)

    def test_long_calculate_position(self) -> None:
        moves = file_read_helper('long_input.txt')
        horz, depth = self.solution.calculate_position(moves)
        self.assertEqual(horz, 1998)
        self.assertEqual(depth, 642047)

def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
