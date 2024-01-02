"""
Level order traversal of binary tree

Problem Statement: Given the root of a binary tree, display the node values at each level."""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class LevelOrderTraversal:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = deque([root])

        while queue:
            level_values = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)

        return result


# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Create an instance of LevelOrderTraversal
lot = LevelOrderTraversal()

# Perform level order traversal
result = lot.level_order(root)

# Print the result
print(result)
