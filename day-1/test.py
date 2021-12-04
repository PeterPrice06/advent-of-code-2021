import unittest
from typing import List
import solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = solution.Solution()

    def test_simple_count_increases(self) -> None:
        depths = file_read_helper('simple_input.txt')
        result = self.solution.count_increases(depths)
        self.assertEqual(result, 7)

    def test_long_count_increases(self) -> None:
        depths = file_read_helper('long_input.txt')
        result = self.solution.count_increases(depths)
        self.assertEqual(result, 1393)

    def test_simple_window_increases(self) -> None:
        depths = file_read_helper('simple_input.txt')
        result = self.solution.count_window_increases(depths, 3)
        self.assertEqual(result, 5)

    def test_long_window_increases(self) -> None:
        depths = file_read_helper('long_input.txt')
        result = self.solution.count_window_increases(depths, 3)
        self.assertEqual(result, 1359)

def file_read_helper(filename: str) -> List[int]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(int(line.strip()))
    return lines

if __name__ == '__main__':
    unittest.main()
