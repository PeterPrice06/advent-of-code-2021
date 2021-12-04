from typing import List, Tuple

FORWARD_KEY = 'forward '
DOWN_KEY = 'down '
UP_KEY = 'up '

class Solution:
    def __init__(self):
        pass

    def calculate_position(self, moves: List[str]) -> Tuple[int, int]:
        horz = 0
        depth = 0
        aim = 0
        for move in moves:
            if move.startswith(FORWARD_KEY):
                distance = int(move[len(FORWARD_KEY):])
                horz += distance
                depth += aim * distance
            elif move.startswith(DOWN_KEY):
                distance = int(move[len(DOWN_KEY):])
                aim += distance
            elif move.startswith(UP_KEY):
                distance = int(move[len(UP_KEY):])
                aim -= distance

        return horz, depth

    def calculate_naive_movement_position(self, moves: List[str]) -> Tuple[int, int]:
        horz = 0
        depth = 0
        for move in moves:
            if move.startswith(FORWARD_KEY):
                distance = int(move[len(FORWARD_KEY):])
                horz += distance
            elif move.startswith(DOWN_KEY):
                distance = int(move[len(DOWN_KEY):])
                depth += distance
            elif move.startswith(UP_KEY):
                distance = int(move[len(UP_KEY):])
                depth -= distance

        return horz, depth
