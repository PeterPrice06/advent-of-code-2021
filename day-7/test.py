import unittest
from typing import List
from crab_alignment import CrabAlignment 

class TestCrabAlignment(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_crab_alignment_median_sample(self) -> None:
        lines = file_read_helper('day-7/sample_input.txt')
        crab_alignment = CrabAlignment(lines)
        self.assertEqual(crab_alignment.best_crab_position_naive(), 2)

    def test_crab_alignment_fuel_to_median_sample(self) -> None:
        lines = file_read_helper('day-7/sample_input.txt')
        crab_alignment = CrabAlignment(lines)
        self.assertEqual(crab_alignment.fuel_to_alignment_naive(), 37)

    def test_crab_alignment_fuel_to_median_puzzle(self) -> None:
        lines = file_read_helper('day-7/puzzle_input.txt')
        crab_alignment = CrabAlignment(lines)
        self.assertEqual(crab_alignment.fuel_to_alignment_naive(), 326132)

    def test_crab_alignment_fuel_to_alignment_sample(self) -> None:
        lines = file_read_helper('day-7/sample_input.txt')
        crab_alignment = CrabAlignment(lines)
        self.assertEqual(crab_alignment.fuel_to_alignment_mean(), 168)

    def test_crab_alignment_fuel_to_alignment_puzzle(self) -> None:
        lines = file_read_helper('day-7/puzzle_input.txt')
        crab_alignment = CrabAlignment(lines)
        self.assertEqual(crab_alignment.fuel_to_alignment_mean(), 88612611) # 88612508 or 88612611



def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
