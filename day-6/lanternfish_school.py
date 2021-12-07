from typing import List

class LanternfishSchool():
    def __init__(self, line_strs: List[str]) -> None:
        self.map = {}

        for lanternfish_countdown_str in line_strs[0].split(','):
            lanternfish_countdown = int(lanternfish_countdown_str, 10)
            if lanternfish_countdown not in self.map:
                self.map[lanternfish_countdown] = 1
            else:
                self.map[lanternfish_countdown] += 1

    def __str__(self) -> str:
        string = ''
        for lanternfish_countdown, lanternfish_count in self.map.items():
            string += f'{lanternfish_countdown}' * lanternfish_count 
        return string

    def age(self) -> int:
        new_map = {}
        for lanternfish_countdown, lanternfish_count in self.map.items():
            if lanternfish_countdown == 0:
                self.map_add_or_create(new_map, 6, lanternfish_count)
                self.map_add_or_create(new_map, 8, lanternfish_count)
            else:
                self.map_add_or_create(new_map, lanternfish_countdown - 1, lanternfish_count)
        self.map = new_map

    def map_add_or_create(self, my_map: map, key: int, value: int) -> None:
        if key in my_map:
            my_map[key] += value
        else:
            my_map[key] = value
                
    def num_fish(self) -> int:
        return sum(self.map.values())
        