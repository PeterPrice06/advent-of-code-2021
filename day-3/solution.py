from typing import List, Tuple

class BinaryTree():
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.print_tree()
    
    def print_tree(self, level=0) -> str:
        string = ''
        if self.left != None:
            string += self.left.print_tree(level + 1) + '\n'
        string += ' ' * 4 * level + '->' + str(self.value) + '\n'
        if self.right != None:
            string += self.right.print_tree(level + 1) + '\n'
        return string

class Solution:
    def __init__(self):
        pass

    def get_gamma_epsilon(self, binaries: List[str]) -> Tuple[int, int]:
        count = 0
        sums = [0] * len(binaries[0])
        for binary in binaries:
            count += 1
            for i, bit in enumerate(binary):
                sums[i] += int(bit, 2)
       
        gamma = 0
        epsilon = 0
        for i, bit_sum in enumerate(reversed(sums)):
            if (bit_sum > count / 2):
                gamma += 1 << i 
            else:
                epsilon += 1 << i 
        return gamma, epsilon

    def get_ratings(self, binaries: List[str]) -> Tuple[int, int]:
        tree = BinaryTree(0)
        for binary_str in binaries:
            tree = self.insert(tree, binary_str)
        # print(tree)

        oxygen_str = self.get_most_common(tree)
        co2_str = self.get_least_common(tree)

        return int(oxygen_str, 2), int(co2_str, 2)

    def insert(self, tree: BinaryTree, value: str) -> BinaryTree:
        if tree is None:
            tree = BinaryTree(0)
        tree.value += 1
        if value == '':
            return tree
        if value[0] == '0':
            tree.left = self.insert(tree.left, value[1:])
        elif value[0] == '1':
            tree.right = self.insert(tree.right, value[1:])
        return tree

    def get_most_common(self, tree: BinaryTree) -> str:
        if tree.left is None and tree.right is None:
            return ''
        if tree.left is None:
            return '1' + self.get_most_common(tree.right)
        if tree.right is None:
            return '0' + self.get_most_common(tree.left)
        if tree.left.value < tree.right.value:
            return '1' + self.get_most_common(tree.right)
        if tree.left.value > tree.right.value:
            return '0' + self.get_most_common(tree.left)
        return '1' + self.get_most_common(tree.right)
 
    def get_least_common(self, tree: BinaryTree) -> str:
        if tree.left is None and tree.right is None:
            return ''
        if tree.left is None:
            return '1' + self.get_least_common(tree.right)
        if tree.right is None:
            return '0' + self.get_least_common(tree.left)
        if tree.left.value > tree.right.value:
            return '1' + self.get_least_common(tree.right)
        if tree.left.value < tree.right.value:
            return '0' + self.get_least_common(tree.left)
        else:
            return '0' + self.get_least_common(tree.left)
           