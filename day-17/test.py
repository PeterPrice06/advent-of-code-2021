import unittest
from typing import List
from cannon import Cannon

class TestCaveNavigator(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_hits_sample(self) -> None:
        lines = file_read_helper('day-17/sample_input.txt')
        cannon = Cannon(lines)
        self.assertEqual(cannon.hits(7, 2), True)
        self.assertEqual(cannon.hits(6, 9), True)

    def test_highest_height_sample(self) -> None:
        lines = file_read_helper('day-17/sample_input.txt')
        cannon = Cannon(lines)
        self.assertEqual(cannon.highest_height(6, 9), 45)



    # def test_highest_hit_sample(self) -> None:
    #     lines = file_read_helper('day-17/sample_input.txt')
    #     cannon = Cannon(lines)
    #     (x, y, max_y) = cannon.highest_hit()
    #     self.assertEqual(x, 6)
    #     self.assertEqual(y, 9)
    #     self.assertEqual(max_y, 45)
    def test_hits_puzzle(self) -> None:
        lines = file_read_helper('day-17/puzzle_input.txt')
        cannon = Cannon(lines)
        hit = False
        optimum_x = 0
        optimum_y = 0
        heighest_height = 0
        for x in range(23, 24):
            for y in range(0, 100):
                if cannon.hits(x, y):
                    hit = True
                    print(f'{x}, {y}')
                    hh = cannon.highest_height(x, y)
                    if heighest_height < hh:
                        heighest_height = hh
                        optimum_x = x
                        optimum_y = y
        print(f'{optimum_x}, {optimum_y}, {heighest_height}')
        self.assertEqual(cannon.hits(optimum_x, optimum_y), True)

    def test_hits_puzzle(self) -> None:
        lines = file_read_helper('day-17/puzzle_input.txt')
        cannon = Cannon(lines)
        hits = 0
        for x in range(20, 500):
            for y in range(-100, 100):
                if cannon.hits(x, y):
                    hits += 1 
                    print(f'{x}, {y}')
        self.assertEqual(hits, 1334) # 194 too low

    def test_hits_sample(self) -> None:
        lines = file_read_helper('day-17/sample_input.txt')
        cannon = Cannon(lines)
        hits = 0
        for x in range(0, 100):
            for y in range(-100, 100):
                if cannon.hits(x, y):
                    hits += 1 
                    print(f'{x}, {y}')
        self.assertEqual(hits, 112)








def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
