from typing import List, Tuple

class Solution:
    def __init__(self):
        self.FORWARD_KEY = 'forward '
        self.DOWN_KEY = 'down '
        self.UP_KEY = 'up '
        pass

    def calculate_position(self, moves: List[str]) -> Tuple[int, int]:
        horz = 0
        depth = 0
        aim = 0
        for i, move in enumerate(moves):
            if move.startswith(self.FORWARD_KEY):
                distance = int(move[len(self.FORWARD_KEY):])
                horz += distance
                depth += aim * distance
            elif move.startswith(self.DOWN_KEY):
                distance = int(move[len(self.DOWN_KEY):])
                aim += distance
            elif move.startswith(self.UP_KEY):
                distance = int(move[len(self.UP_KEY):])
                aim -= distance
 
        return horz, depth

    def calculate_naive_movement_position(self, moves: List[str]) -> Tuple[int, int]:
        horz = 0
        depth = 0
        for i, move in enumerate(moves):
            if move.startswith(self.FORWARD_KEY):
                distance = int(move[len(self.FORWARD_KEY):])
                horz += distance
            elif move.startswith(self.DOWN_KEY):
                distance = int(move[len(self.DOWN_KEY):])
                depth += distance
            elif move.startswith(self.UP_KEY):
                distance = int(move[len(self.UP_KEY):])
                depth -= distance
 
        return horz, depth