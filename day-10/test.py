import unittest
from typing import List
from syntax_checker import SyntaxChecker

class TestSyntaxChecker(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_syntax_error_score_sample(self) -> None:
        lines = file_read_helper('day-10/sample_input.txt')
        syntax_checker = SyntaxChecker(lines)
        self.assertEqual(syntax_checker.error_score(), 26397)

    def test_syntax_error_score_puzzle(self) -> None:
        lines = file_read_helper('day-10/puzzle_input.txt')
        syntax_checker = SyntaxChecker(lines)
        self.assertEqual(syntax_checker.error_score(), 339477)

    def test_syntax_error_score_sample(self) -> None:
        lines = file_read_helper('day-10/sample_input.txt')
        syntax_checker = SyntaxChecker(lines)
        self.assertEqual(syntax_checker.autocomplete_score(), 288957)

    def test_syntax_error_score_puzzle(self) -> None:
        lines = file_read_helper('day-10/puzzle_input.txt')
        syntax_checker = SyntaxChecker(lines)
        self.assertEqual(syntax_checker.autocomplete_score(), 3049320156)





def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
