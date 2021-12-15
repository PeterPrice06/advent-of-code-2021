from typing import List, Set, Dict

class PolymerExtruder():
    def __init__(self, line_strs: List[str]) -> None:
        self.polymer_template = line_strs[0]
        self.insertion_rules = []
        self.polymer = self.polymer_template

        for line_str in line_strs[2:]:
            split_line = line_str.split(' -> ')
            self.insertion_rules.append((split_line[0], split_line[1]))
    
    def extrude(self) -> None:
        new_polymer = ''
        for i in range(len(self.polymer) - 1):
            new_polymer += self.polymer[i]
            for rule in self.insertion_rules:
                polymer_segment = self.polymer[i:i + len(rule[0])]
                if polymer_segment == rule[0]:
                    new_polymer += rule[1]
        new_polymer += polymer_segment[1]
        self.polymer = new_polymer

    def extrude_multiple(self, count: int) -> None:
        for i in range(count):
            print(f'Step {i}: {self.polymer_score()}')
            self.extrude()


    def polymer_score(self) -> int:
        return self.polymer_max_score() - self.polymer_min_score()

    def polymer_max_score(self) -> int:
        counts = self.polymer_char_counts()
        return max(counts.values())

    def polymer_min_score(self) -> int:
        counts = self.polymer_char_counts()
        return min(counts.values())
        
    def polymer_char_counts(self) -> Dict[str, int]:
        counts = {}
        for char in self.polymer:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        return counts