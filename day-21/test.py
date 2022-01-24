import unittest
from typing import List
from dirac_dice import DiracDice, QuantumDiracDice

class TestCaveNavigator(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_play_game_sample(self) -> None:
        lines = file_read_helper('day-21/sample_input.txt')
        dirac_dice = DiracDice(lines)
        dirac_dice.play_game()
        self.assertEqual(dirac_dice.player_2_score, 745)
        self.assertEqual(dirac_dice.num_die_roles, 993)
        self.assertEqual(dirac_dice.player_2_score * dirac_dice.num_die_roles, 739785)

    def test_play_game_puzzle(self) -> None:
        lines = file_read_helper('day-21/puzzle_input.txt')
        dirac_dice = DiracDice(lines)
        dirac_dice.play_game()
        self.assertEqual(min(dirac_dice.player_1_score, dirac_dice.player_2_score) * dirac_dice.num_die_roles, 900099)
        
    def test_play_quantum_game_sample(self) -> None:
        lines = file_read_helper('day-21/sample_input.txt')
        dirac_dice = QuantumDiracDice(lines)
        dirac_dice.play_game()
        self.assertEqual(dirac_dice.player_1_wins, 444356092776315)
        self.assertEqual(dirac_dice.player_2_wins, 341960390180808)
        self.assertEqual(max(dirac_dice.player_1_wins, dirac_dice.player_2_wins), 444356092776315)

    # def test_play_quantum_game_puzzle(self) -> None:
    #     lines = file_read_helper('day-21/puzzle_input.txt')
    #     dirac_dice = QuantumDiracDice(lines)
    #     dirac_dice.play_game()
    #     self.assertEqual(max(dirac_dice.player_1_wins, dirac_dice.player_2_wins), -1)









def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
