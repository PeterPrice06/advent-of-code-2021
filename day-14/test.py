import unittest
from typing import List
from polymer import PolymerExtruder 

class TestCaveNavigator(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_extrude_polymer_once(self) -> None:
        lines = file_read_helper('day-14/sample_input.txt')
        polymer_extruder = PolymerExtruder(lines)
        polymer_extruder.extrude()
        self.assertEqual(polymer_extruder.polymer, 'NCNBCHB')

    def test_extrude_polymer_four_times(self) -> None:
        lines = file_read_helper('day-14/sample_input.txt')
        polymer_extruder = PolymerExtruder(lines)
        polymer_extruder.extrude_multiple(4)
        self.assertEqual(polymer_extruder.polymer, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

    def test_extrude_polymer_ten_times(self) -> None:
        lines = file_read_helper('day-14/sample_input.txt')
        polymer_extruder = PolymerExtruder(lines)
        polymer_extruder.extrude_multiple(10)
        self.assertEqual(polymer_extruder.polymer_max_score(), 1749)
        self.assertEqual(polymer_extruder.polymer_min_score(), 161)
        self.assertEqual(polymer_extruder.polymer_score(), 1588)

    def test_extrude_puzzle_polymer_ten_times(self) -> None:
        lines = file_read_helper('day-14/puzzle_input.txt')
        polymer_extruder = PolymerExtruder(lines)
        polymer_extruder.extrude_multiple(10)
        self.assertEqual(polymer_extruder.polymer_score(), 3284)

    #def test_extrude_sample_polymer_fourty_times(self) -> None:
    #    lines = file_read_helper('day-14/sample_input.txt')
    #    polymer_extruder = PolymerExtruder(lines)
    #    polymer_extruder.extrude_multiple(40)
    #    self.assertEqual(polymer_extruder.polymer_score(), 2188189693529)

    #def test_extrude_puzzle_polymer_fourty_times(self) -> None:
    #    lines = file_read_helper('day-14/puzzle_input.txt')
    #    polymer_extruder = PolymerExtruder(lines)
    #    polymer_extruder.extrude_multiple(40)
    #    self.assertEqual(polymer_extruder.polymer_score(), -1)









def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
