from typing import List, Tuple

class SyntaxChecker():
    def __init__(self, line_strs: List[str]) -> None:
        self.lines = line_strs

        self.first_illegal_character_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.autocomplete_char_score = {'(': 1, '[': 2, '{': 3, '<': 4}

    def error_score(self) -> int:
        score = 0
        for line in self.lines:
            score += self.score_line(line)
        return score

    def score_line(self, line: str) -> int:
        score = 0
        stack = []
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif char == ')' or char == ']' or char == '}' or char == '>':
                prev_char = stack.pop()
                if prev_char == '(' and char != ')' or \
                    prev_char == '[' and char != ']' or \
                    prev_char == '{' and char != '}' or \
                    prev_char == '<' and char != '>':
                    score += self.first_illegal_character_score[char]
        return score
    
    def autocomplete_score(self) -> int:
        scores = []
        for line in self.lines:
            if self.score_line(line) > 0:
                continue
            scores.append(self.autocomplete_line(line))
        return median(scores)

    def autocomplete_line(self, line: str) -> int:
        stack = []
        score = 0
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif char == ')' or char == ']' or char == '}' or char == '>':
                _ = stack.pop()
        while len(stack) > 0:
            char = stack.pop()
            score *= 5
            score += self.autocomplete_char_score[char]
        return score
 
def median(numbers: List[int]) -> int:
    numbers.sort()
    return numbers[len(numbers)//2] 