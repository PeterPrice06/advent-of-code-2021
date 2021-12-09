from typing import List, Tuple

class MinFinder():
    def __init__(self, line_strs: List[str]) -> None:
        self.heights = [line_str for line_str in line_strs]

    def __str__(self) -> str:
        string = ''
        for row in self.heights:
            string += ''.join(row) + '\n'
        return string

    def get_mins(self) -> List[Tuple[int, int]]:
        local_mins = []
        for r in range(len(self.heights)):
            for c in range(len(self.heights[r])):
                if self.is_min(r, c):
                    local_mins.append((r, c))
        return local_mins

    def is_min(self, r: int, c: int) -> bool:
        height = self.heights[r][c]
        if self.is_in_map(r - 1, c) and self.heights[r - 1][c] <= height:
            return False
        if self.is_in_map(r, c - 1) and self.heights[r][c - 1] <= height:
            return False
        if self.is_in_map(r + 1, c) and self.heights[r + 1][c] <= height:
            return False
        if self.is_in_map(r, c + 1) and self.heights[r][c + 1] <= height:
            return False
        return True
    
    def risk_level(self) -> int:
        local_mins = self.get_mins()
        total_risk = 0
        for r, c in local_mins:
            risk = 1 + int(self.heights[r][c]) 
            total_risk += risk
        return total_risk

    def find_basins(self) -> int:
        local_mins = self.get_mins()
        largest_basin_sizes = [0] * 3
        for r, c in local_mins:
            basin_size = self.basin_size(r, c)
            print(basin_size)
            if basin_size > min(largest_basin_sizes):
                largest_basin_sizes.remove(min(largest_basin_sizes))
                largest_basin_sizes.append(basin_size)
        print(largest_basin_sizes)
        return largest_basin_sizes[0] * largest_basin_sizes[1] * largest_basin_sizes[2]
    
    def basin_size(self, r: int, c: int, visited=set(), prev_height = -1) -> int:
        if (r, c) in visited or not self.is_in_map(r, c) or self.heights[r][c] == '9' or int(self.heights[r][c]) <= prev_height:
            return 0
        visited.add((r, c))
        size = 1
        cur_height = int(self.heights[r][c])
        size += self.basin_size(r - 1, c, visited, cur_height)
        size += self.basin_size(r, c - 1, visited, cur_height)
        size += self.basin_size(r + 1, c, visited, cur_height)
        size += self.basin_size(r, c + 1, visited, cur_height)
        return size
    
    def is_in_map(self, r: int, c: int) -> bool:
        return 0 <= r < len(self.heights) and 0 <= c < len(self.heights[r]) 