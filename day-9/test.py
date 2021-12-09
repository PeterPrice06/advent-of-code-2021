import unittest
from typing import List
from min_finder import MinFinder

class TestDecode(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_find_mins_sample(self) -> None:
        lines = file_read_helper('day-9/sample_input.txt')
        min_finder = MinFinder(lines)
        self.assertEqual(min_finder.risk_level(), 15)

    def test_find_mins_puzzle(self) -> None:
        lines = file_read_helper('day-9/puzzle_input.txt')
        min_finder = MinFinder(lines)
        self.assertEqual(min_finder.risk_level(), 526)

    def test_find_basins_sample(self) -> None:
        lines = file_read_helper('day-9/sample_input.txt')
        min_finder = MinFinder(lines)
        self.assertEqual(min_finder.find_basins(), 1134)

    def test_find_basins_puzzle(self) -> None:
        lines = file_read_helper('day-9/puzzle_input.txt')
        min_finder = MinFinder(lines)
        self.assertEqual(min_finder.find_basins(), 1123524)


def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
