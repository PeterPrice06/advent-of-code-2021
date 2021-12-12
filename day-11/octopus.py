from typing import List, Tuple

class DumboOctopi():
    def __init__(self, line_strs: List[str]) -> None:
        self.octopi_energy = [[int(char) for char in line_strs] for line_strs in line_strs]

    def tick(self) -> int:
        flashes = 0

        # self.increase_energy()
        flashes = self.increase_energy_all()
        self.exhaust_energy()
        
        return flashes
    
    def increase_energy(self) -> None:
        for row in range(len(self.octopi_energy)):
            for col in range(len(self.octopi_energy[row])):
                self.octopi_energy[row][col] += 1

    def increase_energy_all(self) -> int:
        flashes = 0
        for row in range(len(self.octopi_energy)):
            for col in range(len(self.octopi_energy[row])):
                flashes += self.flash(row, col)

        return flashes

    def flash(self, row: int, col: int) -> int:
        if not self.in_bounds(row, col):
            return 0
        self.octopi_energy[row][col] += 1
        if self.octopi_energy[row][col] == 9 + 1:
            flashes = 1
            flashes += self.flash(row - 1, col)
            flashes += self.flash(row, col - 1)
            flashes += self.flash(row + 1, col)
            flashes += self.flash(row, col + 1)
            flashes += self.flash(row - 1, col - 1)
            flashes += self.flash(row + 1, col - 1)
            flashes += self.flash(row + 1, col + 1)
            flashes += self.flash(row - 1, col + 1)
            return flashes 
        return 0
    
    def exhaust_energy(self) -> None:
        for row in range(len(self.octopi_energy)): 
            for col in range(len(self.octopi_energy[row])):
                if self.octopi_energy[row][col] > 9:
                    self.octopi_energy[row][col] = 0

    def in_bounds(self, row: int, col: int) -> bool:
        if row >= 0 and row < len(self.octopi_energy) and col >= 0 and col < len(self.octopi_energy[row]):
            return True
        else:
            return False

    def __str__(self) -> str:
        # print the octopi energy levels with a newline after each row and no space between columns
        return '\n'.join([''.join([str(char) for char in row]) for row in self.octopi_energy])