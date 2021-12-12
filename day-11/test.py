import unittest
from typing import List
from octopus import DumboOctopi

class TestDumboOctopi(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_dumbo_octopus_sample(self) -> None:
        lines = file_read_helper('day-11/sample_input.txt')
        dumbo_octopi = DumboOctopi(lines)
        flashes = 0
        for i in range(100):
            flashes += dumbo_octopi.tick()
        self.assertEqual(flashes, 1656)

    def test_dumbo_octopus_puzzle(self) -> None:
        lines = file_read_helper('day-11/puzzle_input.txt')
        dumbo_octopi = DumboOctopi(lines)
        flashes = 0
        for i in range(100):
            flashes += dumbo_octopi.tick()
        self.assertEqual(flashes, 1647)

    def test_dumbo_octopus_sync_sample(self) -> None:
        lines = file_read_helper('day-11/sample_input.txt')
        dumbo_octopi = DumboOctopi(lines)
        i = 1
        max_flash = len(dumbo_octopi.octopi_energy) * len(dumbo_octopi.octopi_energy[0])
        flash = dumbo_octopi.tick()
        while i < 100000 and flash != max_flash:
            flash = dumbo_octopi.tick()
            i += 1
        self.assertEqual(i, 195)

    def test_dumbo_octopus_sync_puzzle(self) -> None:
        lines = file_read_helper('day-11/puzzle_input.txt')
        dumbo_octopi = DumboOctopi(lines)
        i = 1
        max_flash = len(dumbo_octopi.octopi_energy) * len(dumbo_octopi.octopi_energy[0])
        flash = dumbo_octopi.tick()
        while i < 100000 and flash != max_flash:
            flash = dumbo_octopi.tick()
            i += 1
        self.assertEqual(i, 348)

def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
