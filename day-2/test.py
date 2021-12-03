import unittest
import solution
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = solution.Solution()
        pass

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
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()