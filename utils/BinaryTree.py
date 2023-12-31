class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_binary_tree(arr, index=0):
    if index < len(arr):
        if arr[index] is None:
            return None

        root = TreeNode(arr[index])
        root.left = array_to_binary_tree(arr, 2 * index + 1)
        root.right = array_to_binary_tree(arr, 2 * index + 2)

        return root
    return None
