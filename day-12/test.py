import unittest
from typing import List
from cave_navigator import CaveNavigator 

class TestCaveNavigator(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_cave_navigator_small_sample(self) -> None:
        lines = file_read_helper('day-12/small_sample_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(), 10)

    def test_cave_navigator_medium_sample(self) -> None:
        lines = file_read_helper('day-12/medium_sample_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(), 19)

    def test_cave_navigator_large_sample(self) -> None:
        lines = file_read_helper('day-12/large_sample_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(), 226)

    def test_cave_navigator_puzzle(self) -> None:
        lines = file_read_helper('day-12/puzzle_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(), 3497)

    def test_cave_navigator_enabled_extra_visit_small_sample(self) -> None:
        lines = file_read_helper('day-12/small_sample_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(allow_extra_visit=True), 36)

    def test_cave_navigator_enabled_extra_visit_medium_sample(self) -> None:
        lines = file_read_helper('day-12/medium_sample_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(allow_extra_visit=True), 103)

    def test_cave_navigator_enabled_extra_visit_large_sample(self) -> None:
        lines = file_read_helper('day-12/large_sample_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(allow_extra_visit=True), 3509)

    def test_cave_navigator_enabled_extra_visit_puzzle(self) -> None:
        lines = file_read_helper('day-12/puzzle_input.txt')
        cave_navigator = CaveNavigator(lines)
        self.assertEqual(cave_navigator.count_paths(allow_extra_visit=True), 93686)



def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
