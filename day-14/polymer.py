from typing import List, Set, Dict

class PolymerExtruder():
    def __init__(self, line_strs: List[str]) -> None:
        self.polymer_template = line_strs[0]
        self.insertion_rules = []
        self.polymer_pairs = {}
        for i in range(len(self.polymer_template) - 1):
            pair = self.polymer_template[i:i + 2]
            if pair not in self.polymer_pairs:
                self.polymer_pairs[pair] = 1
            else:
                self.polymer_pairs[pair] += 1

        for line_str in line_strs[2:]:
            split_line = line_str.split(' -> ')
            self.insertion_rules.append((split_line[0], split_line[1]))
    
    def extrude(self) -> None:
        new_polymer_pairs = {}
        for rule in self.insertion_rules:
            if rule[0] in self.polymer_pairs:
                pair_count = self.polymer_pairs[rule[0]]
                new_pair_first_half = rule[0][0] + rule[1]
                if new_pair_first_half not in new_polymer_pairs:
                    new_polymer_pairs[new_pair_first_half] = pair_count
                else:
                    new_polymer_pairs[new_pair_first_half] += pair_count
                new_pair_second_half = rule[1] + rule[0][1]
                if new_pair_second_half not in new_polymer_pairs:
                    new_polymer_pairs[new_pair_second_half] = pair_count
                else:
                    new_polymer_pairs[new_pair_second_half] += pair_count
        self.polymer_pairs = new_polymer_pairs.copy()
            
    def extrude_multiple(self, count: int) -> None:
        for i in range(count):
            print(f'Step {i}: {self.polymer_score()}\t| {self.polymer_pairs}')
            self.extrude()

    def polymer_score(self) -> int:
        counts = self.polymer_char_counts()
        return max(counts.values()) - min(counts.values())

    def polymer_char_counts(self) -> Dict[str, int]:
        counts = {}
        for pair in self.polymer_pairs:
            char = pair[0]
            if char not in counts:
                counts[char] = self.polymer_pairs[pair]
            else:
                counts[char] += self.polymer_pairs[pair]
        return counts