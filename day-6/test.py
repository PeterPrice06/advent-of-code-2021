import unittest
from typing import List
from lanternfish_school import LanternfishSchool 

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_lanternfish_school_sample_quick(self) -> None:
        lines = file_read_helper('day-6/sample_input.txt')
        lanternfish_school = LanternfishSchool(lines)
        for _ in range(0, 18):
            lanternfish_school.age()
        self.assertEqual(lanternfish_school.num_fish(), 26)

    def test_lanternfish_school_sample(self) -> None:
        lines = file_read_helper('day-6/sample_input.txt')
        lanternfish_school = LanternfishSchool(lines)
        for _ in range(0, 80):
            lanternfish_school.age()
        self.assertEqual(lanternfish_school.num_fish(), 5934)

    def test_lanternfish_school_puzzle(self) -> None:
        lines = file_read_helper('day-6/puzzle_input.txt')
        lanternfish_school = LanternfishSchool(lines)
        for _ in range(0, 80):
            lanternfish_school.age()
        self.assertEqual(lanternfish_school.num_fish(), 359344)

    def test_lanternfish_school_sample(self) -> None:
        lines = file_read_helper('day-6/sample_input.txt')
        lanternfish_school = LanternfishSchool(lines)
        for _ in range(0, 256):
            lanternfish_school.age()
        self.assertEqual(lanternfish_school.num_fish(), 26984457539)

    def test_lanternfish_school_puzzle(self) -> None:
        lines = file_read_helper('day-6/puzzle_input.txt')
        lanternfish_school = LanternfishSchool(lines)
        for _ in range(0, 256):
            lanternfish_school.age()
        self.assertEqual(lanternfish_school.num_fish(), -1)



def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
