from typing import List, Tuple, Set

class PaperFolder():
    def __init__(self, line_strs: List[str]) -> None:
        self.dots = set()
        self.folds = []

        for line_str in line_strs:
            if ',' in line_str:
                split_line = line_str.split(',')
                self.dots.add((int(split_line[0]), int(split_line[1])))
            elif 'fold along' in line_str:
                split_line = line_str.split('=')
                self.folds.append((split_line[0], int(split_line[1])))

    def __str__(self) -> str:
        string = '\n'
        for y in range(self.max_y() + 1):
            for x in range(self.max_x() + 1):
                if (x, y) in self.dots:
                    string += '#'
                else:
                    string += '.'
            string += '\n'
        return string 

    def max_x(self) -> int:
        return max(self.dots, key=lambda x: x[0])[0]
    
    def max_y(self) -> int:
        return max(self.dots, key=lambda x: x[1])[1]

    def fold_all(self) -> None:
        self.fold(len(self.folds))

    def fold(self, num_folds=0) -> Set[Tuple[int, int]]:
        for fold in self.folds[:num_folds]:
            new_dots = set()
            for dot in self.dots:
                if fold[0] == 'fold along x':
                    new_x = self.calculate_fold(fold[1], dot[0])
                    new_dots.add((new_x, dot[1]))
                elif fold[0] == 'fold along y':
                    new_y = self.calculate_fold(fold[1], dot[1])
                    new_dots.add((dot[0], new_y))
                else:
                    print('Error: unknown fold type')
            self.dots = new_dots.copy()
        return new_dots

    def calculate_fold(self, fold_num: int, dot_num: int) -> int:
        if fold_num > dot_num:
            return dot_num
        return fold_num - (dot_num - fold_num) 

    #         y    f    d
    #         8   10   12
    

    def count_dots(self) -> int:
        return len(self.dots)