from typing import List, Set, Dict, Tuple

class DiracDice():
    def __init__(self, line_strs: List[str]) -> None:
        self.player_1_start = int(line_strs[0].split(': ')[-1])
        self.player_2_start = int(line_strs[1].split(': ')[-1])
        self.player_1_pos = self.player_1_start
        self.player_2_pos = self.player_2_start
        self.player_1_score = 0
        self.player_2_score = 0
        self.deterministic_dice_counter = 0
        self.deterministic_dice_rollover = 100
        self.num_die_roles = 0
        self.num_spaces = 10
        self.winning_score = 1000
    
    def roll(self) -> int:
        cur_role = self.deterministic_dice_counter + 1
        self.num_die_roles += 1
        self.deterministic_dice_counter = (self.deterministic_dice_counter + 1) % self.deterministic_dice_rollover
        return cur_role
    
    def move_player_1(self, dice: int) -> None:
        self.player_1_pos = ((self.player_1_pos - 1 + dice) % self.num_spaces) + 1
        self.player_1_score += self.player_1_pos
    
    def move_player_2(self, dice: int) -> None:
        self.player_2_pos = ((self.player_2_pos - 1 + dice) % self.num_spaces) + 1
        self.player_2_score += self.player_2_pos

    def play_game(self) -> bool:
        is_player_1_turn = True
        while self.player_1_score < self.winning_score and self.player_2_score < self.winning_score:
            #print(f'Player 1: {self.player_1_score}, Player 2: {self.player_2_score}')
            rolls = self.roll() + self.roll() + self.roll()
            #print(f'Rolls: {rolls}')
            if is_player_1_turn:
                self.move_player_1(rolls)
            else:
                self.move_player_2(rolls)
            is_player_1_turn = not is_player_1_turn

#                      1
#    1 2 3 4 5 6 7 8 9 0
# 0|       x       y      x = 0        , y = 0
# 1|         x x x y      x = (5, 6, 7), y = 0
# 2| y       x x x   y y  x = (5, 6, 7), y = (9, 10, 1))

#                  x
#                x x x
#              x x x x x  x = (5 + 6, 5 + 7, 5 + 8, 6 + 7, 6 + 8, 6 + 9, 7 + 8, 7 + 9, 7 + 10) y = (9, 10, 1)
# 3| y               y y  x = (11   , 12   , 13   , 13   , 14   , 15   , 15   , 16   , 17    ) y = (9, 10, 1)

# 1 + 1 + 1 = 3
# 1 + 1 + 2 = 4
# 1 + 1 + 3 = 5
# 1 + 2 + 1 = 4
# 1 + 2 + 2 = 5
# 1 + 2 + 3 = 6        3 4 4 5 5 5 6 6 6 6 6 7 7 7 8 8 9
# 1 + 3 + 1 = 5
# 1 + 3 + 2 = 6
# 1 + 3 + 3 = 7
#...
class QuantumDiracDice():
    def __init__(self, line_strs: List[str]) -> None:
        self.player_1_start = int(line_strs[0].split(': ')[-1])
        self.player_2_start = int(line_strs[1].split(': ')[-1])
        self.player_1_pos = self.player_1_start
        self.player_2_pos = self.player_2_start
        self.states = {}
        self.player_1_location_index = 0
        self.player_1_score_index = 1
        self.player_2_location_index = 2
        self.player_2_score_index = 3
        self.is_player_1_turn_index = 4
        self.num_spaces = 10
        self.winning_score = 21
        self.player_1_wins = 0
        self.player_2_wins = 0
    
    def calculate_move(self, location: int, move: int) -> int:
        new_location = (location - 1 + move) % self.num_spaces + 1
        return new_location
    
    def move_player_1(self, state: Tuple[int, int, int, int, bool], games: int) -> None:
        for move, frequency in ((3, 1), (4, 2), (5, 3), (6, 4), (7, 3), (8, 2), (9, 1)):
            new_pos = self.calculate_move(state[self.player_1_location_index], move)
            self.states[(new_pos, state[1] + new_pos, state[2], state[3], not state[4])] = games * frequency
    
    def move_player_2(self, state: Tuple[int, int, int, int, bool], games: int) -> None:
        for move, frequency in ((3, 1), (4, 2), (5, 3), (6, 4), (7, 3), (8, 2), (9, 1)):
            new_pos = self.calculate_move(state[self.player_2_location_index], move)
            self.states[(state[0], state[1], new_pos, state[3] + new_pos, not state[4])] = games * frequency

    def play_game(self) -> bool:
        self.states[(self.player_1_start, 0, self.player_2_start, 0, True)] = 1
        while len(self.states) > 0:
            print(f'States: {len(self.states)}, Player 1 wins: {self.player_1_wins}, Player 2 wins: {self.player_2_wins}')
            state, games = self.states.popitem()
            if state[self.player_1_score_index] >= self.winning_score:
                self.player_1_wins += games
                continue
            if state[self.player_2_score_index] >= self.winning_score:
                self.player_2_wins += games
                continue

            if state[self.is_player_1_turn_index]:
                self.move_player_1(state, games)
            else:
                self.move_player_2(state, games)