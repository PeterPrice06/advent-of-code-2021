from typing import List, Dict, Set

class CaveNavigator():
    def __init__(self, line_strs: List[str]) -> None:
        self.adjacency_list = self.build_adjacency_list(line_strs) 

    def build_adjacency_list(self, line_strs: List[str]) -> Dict[str, Set[str]]:
        # build the adjacency list from the cave map
        adjacency_list = {}
        for line_str in line_strs:
            line_parts = line_str.split('-')
            node_a = line_parts[0]
            node_b = line_parts[1]
            if node_a not in adjacency_list: 
                adjacency_list[node_a] = {node_b}
            else:
                adjacency_list[node_a].add(node_b)
            if node_b not in adjacency_list:
                adjacency_list[node_b] = {node_a}
            else:
                adjacency_list[node_b].add(node_a)
        return adjacency_list

    def __str__(self) -> str:
        string = ''
        for node in self.adjacency_list:
            string += f'{node} -> {str(self.adjacency_list[node])}\n'
        return string

    def count_paths(self, allow_extra_visit=False) -> int:
        if allow_extra_visit:
            return self.count_paths_with_extra_visit_recursive('start', 'end', set(), 1)
        return self.count_paths_recursive('start', 'end', set())
    
    def count_paths_recursive(self, node: str, target: str, visited: Set[str]) -> int:
        if node == target:
            return 1
        if node.islower():
            if node in visited:
                return 0
            visited.add(node)
        count = 0
        for neighbor in self.adjacency_list[node]:
            count += self.count_paths_recursive(neighbor, target, visited.copy())
        return count

    def count_paths_with_extra_visit_recursive(self, node: str, target: str, visited: Set[str], extra_visits_left: int) -> int:
        if node == target:
            return 1
        if node.islower():
            if node in visited:
                if extra_visits_left == 0 or node == 'start':
                    return 0
                extra_visits_left -= 1
            else:
                visited.add(node)
        count = 0
        for neighbor in self.adjacency_list[node]:
            count += self.count_paths_with_extra_visit_recursive(neighbor, target, visited.copy(), extra_visits_left)
        return count