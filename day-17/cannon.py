from typing import List, Set, Dict, Tuple

class Cannon():
    def __init__(self, line_strs: List[str]) -> None:
        line_str = line_strs[0]
        x_equals_index = line_str.find('x=')
        y_equals_index = line_str.find(', y=')
        x_range = line_str[x_equals_index+2:y_equals_index].split('..')
        y_range = line_str[y_equals_index+4:].split('..')
        self.x_min = int(x_range[0])
        self.x_max = int(x_range[1])
        self.y_min = int(y_range[0])
        self.y_max = int(y_range[1])

    def hits(self, vel_x: int, vel_y: int) -> bool:
        x, y = 0, 0
        t = 0
        while y >= self.y_min and (abs(vel_x) > 0 or self.x_min <= x <= self.x_max):
            if (self.x_min <= x <= self.x_max) and (self.y_min <= y <= self.y_max):
                return True
            x += vel_x
            y += vel_y
            if vel_x > 0:
                vel_x -= 1
            elif vel_x < 0:
                vel_x += 1
            vel_y -= 1
        return False
    
    def highest_height(self, vel_x: int, vel_y: int) -> bool:
        x, y = 0, 0
        t = 0
        prev_y = 0
        while prev_y <= y:
            prev_y = y
            y += vel_y
            vel_y -= 1
        return prev_y
    
    def highest_hit(self) -> Tuple[int, int, int]:
        vel_x = 0
        vel_y = 0
        while vel_x <= 0:
            vel_x += 1
            while vel_y <= 0:
                vel_y += 1
                if self.hits(vel_x, vel_y):
                    return vel_x, vel_y, t
        return None

# Quickly figure out what lowest vel xs are (23 or 24)
# for i in range(50):
#     sum = 0
#     for j in range(i):
#         sum += j
#     print(f'{i}: sum: {sum}')
#      
# 0: sum: 0
# 1: sum: 0
# 2: sum: 1
# 3: sum: 3
# 4: sum: 6
# 5: sum: 10
# 6: sum: 15
# 7: sum: 21
# 8: sum: 28
# 9: sum: 36
# 10: sum: 45
# 11: sum: 55
# 12: sum: 66
# 13: sum: 78
# 14: sum: 91
# 15: sum: 105
# 16: sum: 120
# 17: sum: 136
# 18: sum: 153
# 19: sum: 171
# 20: sum: 190
# 21: sum: 210
# 22: sum: 231 - lowest speed
# 23: sum: 253
# 24: sum: 276
# 25: sum: 300
# 26: sum: 325
# 27: sum: 351
# 28: sum: 378
# 29: sum: 406
# 30: sum: 435
# 31: sum: 465
# 32: sum: 496
# 33: sum: 528
# 34: sum: 561
# 35: sum: 595
# 36: sum: 630
# 37: sum: 666
# 38: sum: 703
# 39: sum: 741
# 40: sum: 780
# 41: sum: 820
# 42: sum: 861
# 43: sum: 903
# 44: sum: 946
# 45: sum: 990
# 46: sum: 1035
# 47: sum: 1081
# 48: sum: 1128
# 49: sum: 1176