import unittest
from typing import List
from paper_folder import PaperFolder

class TestCaveNavigator(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_fold_sample_paper_1_time(self) -> None:
        lines = file_read_helper('day-13/sample_input.txt')
        paper_folder = PaperFolder(lines)
        paper_folder.fold(1)
        self.assertEqual(paper_folder.count_dots(), 17)

    def test_fold_puzzle_paper_1_time(self) -> None:
        lines = file_read_helper('day-13/puzzle_input.txt')
        paper_folder = PaperFolder(lines)
        paper_folder.fold(1)
        self.assertEqual(paper_folder.count_dots(), 763)

    def test_fold_sample_paper_all_times(self) -> None:
        lines = file_read_helper('day-13/sample_input.txt')
        paper_folder = PaperFolder(lines)
        paper_folder.fold_all()
        self.assertEqual(str(paper_folder), '\n#####\n#...#\n#...#\n#...#\n#####\n')

    def test_fold_puzzle_paper_all_times(self) -> None:
        lines = file_read_helper('day-13/puzzle_input.txt')
        paper_folder = PaperFolder(lines)
        paper_folder.fold_all()
        self.assertEqual(str(paper_folder), '''
###..#..#..##..#....###...##..###...##.
#..#.#..#.#..#.#....#..#.#..#.#..#.#..#
#..#.####.#..#.#....#..#.#....#..#.#..#
###..#..#.####.#....###..#....###..####
#.#..#..#.#..#.#....#.#..#..#.#.#..#..#
#..#.#..#.#..#.####.#..#..##..#..#.#..#
''')

       



def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
