from typing import List

class Solution:
    def __init__(self):
        pass

    def count_increases(self, depths: List[int]) -> int:
        count = 0
        for i in range(len(depths) - 1):
            if depths[i] < depths[i+1]:
                count += 1
        return count 

    def count_window_increases(self, depths: List[int], window: int) -> int:
        count = 0
        for i in range(len(depths) - window):
            if sum(depths[i : i + window]) < sum(depths[i + 1 : i + window +1]):
                count += 1
        return count