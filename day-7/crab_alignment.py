from typing import List

class CrabAlignment():
    def __init__(self, line_strs: List[str]) -> None:
        self.crab_positions = []

        self.crab_positions = list(map(int, line_strs[0].split(',')))
        self.min = min(self.crab_positions)
        self.max = max(self.crab_positions)
        self.max_movement = self.max - self.min

    def __str__(self) -> str:
        return str(self.crab_positions) 

    def best_crab_position_naive(self) -> int:
        # calculate the median of crab positions
        return sorted(self.crab_positions)[len(self.crab_positions) // 2]

    def best_crab_position_mean(self) -> int:
        # calculate the mean of crab positions
        return sum(self.crab_positions) // len(self.crab_positions) 

    def fuel_to_alignment_naive(self) -> int:
        median = self.best_crab_position_naive()
        return sum(abs(crab_position - median) for crab_position in self.crab_positions) 
       
    def fuel_to_alignment_mean(self) -> int:
        mean = self.best_crab_position_mean()
        movement_penalties = self.movement_penalties()
        print(movement_penalties)
        return sum(movement_penalties[abs(crab_position - mean)] for crab_position in self.crab_positions) 
 

    def movement_penalties(self) -> List[int]:
        movement_penalties = [0]
        for i in range(1, self.max_movement):
            movement_penalties.append(i + movement_penalties[i - 1])
        return movement_penalties
    

            


# 1 2 3  4  5  6  7  8  9 10
# 1 3 6 10 15 21 28 36 45 55 sum