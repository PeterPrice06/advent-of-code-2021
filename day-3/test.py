import unittest
from typing import List
import solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = solution.Solution()

    def test_simple_get_gamma_epsilon(self) -> None:
        binaries = file_read_helper('simple_input.txt')

        gamma, epsilon = self.solution.get_gamma_epsilon(binaries)
         
        self.assertEqual(gamma, 22)
        self.assertEqual(epsilon, 9)
        self.assertEqual(gamma * epsilon, 198)

    def test_long_get_gamma_epsilon(self) -> None:
        binaries = file_read_helper('long_input.txt')

        gamma, epsilon = self.solution.get_gamma_epsilon(binaries)

        self.assertEqual(gamma, 3875)
        self.assertEqual(epsilon, 220)
        self.assertEqual(gamma * epsilon, 852500)

    def test_simple_get_ratings(self) -> None:
        binaries = file_read_helper('simple_input.txt')

        oxygen, co2 = self.solution.get_ratings(binaries)
         
        self.assertEqual(oxygen, 23)
        self.assertEqual(co2, 10)
        self.assertEqual(oxygen * co2, 230)

    def test_long_get_ratings(self) -> None:
        binaries = file_read_helper('long_input.txt')

        oxygen, co2 = self.solution.get_ratings(binaries)
         
        self.assertEqual(oxygen, 2235)
        self.assertEqual(co2, 451)
        self.assertEqual(oxygen * co2, 1007985) # toolow 1007534
        


def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
