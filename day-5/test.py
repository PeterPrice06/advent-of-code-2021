import unittest
from typing import List
from lines import VentMap 

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_bingo_sample(self) -> None:
        lines = file_read_helper('day-5/sample_input.txt')
        vent_map = VentMap(lines, include_diagonals=False)
        print(vent_map)
        self.assertEqual(vent_map.count_intersections(), 5)

    def test_bingo_puzzle(self) -> None:
        lines = file_read_helper('day-5/puzzle_input.txt')
        vent_map = VentMap(lines)
        self.assertEqual(vent_map.count_intersections(), 5) # Too high 954034

def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines    

if __name__ == '__main__':
    unittest.main()
