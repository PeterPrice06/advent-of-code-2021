from typing import List, Tuple

class VentMap():
    def __init__(self, line_strs: List[str], include_diagonals=True) -> None:
        self.map = [[0 for i in range(991)] for j in range(991)]
        self.max_x_coord = 0
        self.max_y_coord = 0

        for line_str in line_strs:
            line = Line(line_str, include_diagonals)
            for point in line.points:
                self.max_x_coord = max(self.max_x_coord, point.x)
                self.max_y_coord = max(self.max_y_coord, point.y)
                self.map[point.x][point.y] += 1

    def __str__(self) -> str:
        string = ''
        for y in range(self.max_y_coord + 1):
            for x in range(self.max_x_coord + 1):
                if self.map[x][y] != 0:
                    string += str(self.map[x][y])
                else:
                    string += '.'
            string += '\n'
        return string

    def count_intersections(self) -> int:
        count = 0
        for y in range(self.max_y_coord + 1):
            for x in range(self.max_x_coord + 1):
                if self.map[x][y] > 1:
                    count += 1
        return count

class Line():
    def __init__(self, line_str: str, include_diagonals) -> None:
        self.points = []
        self.include_diagonals = include_diagonals

        self.parse_line(line_str)

    def parse_line(self, line_str: str) -> None:
        string_points = line_str.split(' -> ')
        start_coords = string_points[0].split(',')
        end_coords = string_points[1].split(',')
        start_coords = list(map(int, start_coords))
        end_coords = list(map(int, end_coords))
        self.start = Point(start_coords[0], start_coords[1])
        self.end = Point(end_coords[0], end_coords[1])

        # Get in between points
        smaller_x = min(self.start.x, self.end.x)
        smaller_y = min(self.start.y, self.end.y)
        larger_x = max(self.start.x, self.end.x)
        larger_y = max(self.start.y, self.end.y)

        if smaller_x == larger_x and smaller_y == larger_y:
            self.points.append(Point(smaller_x, smaller_y))
        elif smaller_x == larger_x:
            for y in range(smaller_y, larger_y + 1):
                self.points.append(Point(smaller_x, y))
        elif smaller_y == larger_y:
            for x in range(smaller_x, larger_x + 1):
                self.points.append(Point(x, smaller_y))
        elif self.include_diagonals:
            if self.start.x < self.end.x and self.start.y < self.end.y:
                for i in range(0, larger_x - smaller_x + 1):
                    self.points.append(Point(smaller_x + i, smaller_y + i))
            elif self.start.x > self.end.x and self.start.y < self.end.y:
                for i in range(0, larger_x - smaller_x + 1):
                    self.points.append(Point(larger_x - i, smaller_y + i))
            elif self.start.x < self.end.x and self.start.y > self.end.y:
                for i in range(0, larger_x - smaller_x + 1):
                    self.points.append(Point(smaller_x + i, larger_y - i))
            elif self.start.x > self.end.x and self.start.y > self.end.y:
                for i in range(0, larger_x - smaller_x + 1):
                    self.points.append(Point(larger_x - i, larger_y - i))

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __str__(self) -> str:
        return f'{self.x},{self.y}'
        