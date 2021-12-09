from typing import List, Tuple

class Decoder():
    def __init__(self, line_strs: List[str]) -> None:
        self.signal_patterns = []
        self.output_values = []

        for line in line_strs:
            line_halves = line.split(' | ')
            self.signal_patterns.append(line_halves[0])
            self.output_values.append(line_halves[1])

        self.words = {}
        for signal_pattern_line in self.signal_patterns:
            for word in signal_pattern_line.split():
                if word not in self.words:
                    self.words[word] = 1
                else:
                    self.words[word] += 1
                
        self.words_with_unique_lengths, self.unique_lengths = self.get_unique_lengths()

    def __str__(self) -> str:
        string = f'words: {self.words}\n'
        for i in range(len(self.signal_patterns)):
            string += self.signal_patterns[i] + ' | ' + self.output_values[i] + '\n'
        return string

    def get_unique_lengths(self) -> Tuple[List[str], List[int]]:
        words_with_unique_lengths = []
        unique_lengths = []
        word_length_counts = {}
        for word in self.words.keys():
            if len(word) in word_length_counts:
                word_length_counts[len(word)] += 1
            else:
                word_length_counts[len(word)] = 1
        for word, count in word_length_counts.items():
            if count == 1:
                words_with_unique_lengths.append(word)
                unique_lengths.append(len(word))
        
        return words_with_unique_lengths, unique_lengths

    def count_unique_in_output_value(self) -> int:
        # only count unique in output_value
        count = 0
        for output_value in self.output_values:
            for output_word in output_value.split():
                if self.is_unique(output_word):
                    count += 1
        return count

    def is_unique(self, word: str) -> int:
        # check if word is 1, 4, 7, or 8
        length = len(word)
        return length in [2, 3, 4, 7]

    def sum_decoded_output(self) -> int:
        sum = 0
        for i, output_value in enumerate(self.output_values):
            output = 0
            for output_word in output_value.split():
                output *= 10
                digit = self.decode(output_word, self.signal_patterns[i])
                output += digit 
            print(output)
            sum += output
        return sum

    def decode(self, word: str, signal_patterns: str) -> int:
        if len(word) == 2:
            return 1
        elif len(word) == 3:
            return 7
        elif len(word) == 4:
            return 4
        elif len(word) == 5:
            if self.same_lines_as_one(word, signal_patterns):
                return 3
            elif self.all_but_one_line_of_four(word, signal_patterns):
                return 5
            else: 
                return 2
        elif len(word) == 6:
            if self.same_lines_as_one(word, signal_patterns):
                if self.same_lines_as_four(word, signal_patterns):
                    return 9
                else:
                    return 0
            return 6 
        elif len(word) == 7:
            return 8

    def same_lines_as_one(self, word: str, signal_patterns: str) -> bool:
        for signal_pattern_word in signal_patterns.split():
            if len(signal_pattern_word) == 2:
                return signal_pattern_word[0] in word and signal_pattern_word[1] in word
        print('WARNING: signal pattern does not contain digit 1')
        return False

    def same_lines_as_four(self, word: str, signal_patterns: str) -> bool:
        for signal_pattern_word in signal_patterns.split():
            if len(signal_pattern_word) == 4:
                return signal_pattern_word[0] in word and signal_pattern_word[1] in word and \
                    signal_pattern_word[2] in word and signal_pattern_word[3] in word
        print('WARNING: signal pattern does not contain digit 4')
        return False

    def all_but_one_line_of_four(self, word: str, signal_patterns: str) -> bool:
        for signal_pattern_word in signal_patterns.split():
            if len(signal_pattern_word) == 4:
                return int(signal_pattern_word[0] in word) + int(signal_pattern_word[1] in word) + \
                    int(signal_pattern_word[2] in word) + int(signal_pattern_word[3] in word) == 3
        print('WARNING: signal pattern does not contain digit 4')
        return False
