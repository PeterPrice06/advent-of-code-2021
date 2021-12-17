from typing import List, Set, Dict, Tuple

class Navigator():
    def __init__(self, line_strs: List[str]) -> None:
        self.cave = line_strs 
        

    def a_star(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        A* algorithm to find the shortest path from start to end.
        """
        # Set of nodes already evaluated
        closed_set: Set[Tuple[int, int]] = set()
        # Set of nodes to be evaluated
        open_set: Set[Tuple[int, int]] = set()
        # The set of tentative nodes to be evaluated, initially containing the start node
        open_set.add(start)
        # The map of navigated nodes.
        navigated_nodes: Dict[Tuple[int, int], Tuple[int, int]] = {}
        # The map of g scores.
        g_scores: Dict[Tuple[int, int], int] = {}
        # The map of f scores.
        f_scores: Dict[Tuple[int, int], int] = {}
        # The map of parents.
        parents: Dict[Tuple[int, int], Tuple[int, int]] = {}
        # Initialize g scores and f scores
        g_scores[start] = 0
        f_scores[start] = self.heuristic(start, end)
        # Loop until open set is empty
        while open_set:
            # Get the node in open set with the lowest f score
            current: Tuple[int, int] = min(open_set, key=lambda x: f_scores[x])
            # If the current node is the goal, return the path
            if current == end:
                return self.reconstruct_path(parents, current)
            # Remove the current node from open set
            open_set.remove(current)
            # Add the current node to closed set
            closed_set.add(current)
            # Loop through the neighbors of the current node
            for neighbor in self.neighbors(current):
                # If the neighbor is in closed set, skip
                if neighbor in closed_set:
                    continue
                # If the neighbor is not in open set, add it
                if neighbor not in open_set:
                    open_set.add(neighbor)