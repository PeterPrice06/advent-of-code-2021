import unittest
from typing import List
from decoder import Decoder

class TestDecode(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_decode_count_unique_sample(self) -> None:
        lines = file_read_helper('day-8/sample_input.txt')
        decoder = Decoder(lines)
        self.assertEqual(decoder.count_unique_in_output_value(), 26)

    def test_decode_count_unique_sample(self) -> None:
        lines = file_read_helper('day-8/sample_input.txt')
        decoder = Decoder(lines)
        self.assertEqual(decoder.count_unique_in_output_value(), 26)

    def test_decode_sum_decoded_output_sample(self) -> None:
        lines = file_read_helper('day-8/sample_input.txt')
        decoder = Decoder(lines)
        self.assertEqual(decoder.sum_decoded_output(), 61229)

    def test_decode_sum_decoded_output_puzzle(self) -> None:
        lines = file_read_helper('day-8/puzzle_input.txt')
        decoder = Decoder(lines)
        self.assertEqual(decoder.sum_decoded_output(), 978171)



def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
