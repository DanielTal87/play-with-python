# LeetCode: 606


from typing import Optional

from utils.BinaryTree import TreeNode


class Tree2string:
    id = 606

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        res = []

        def pre_order(root):
            if not root:
                return

            res.append("(")
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")
            pre_order(root.left)
            pre_order(root.right)
            res.append(")")

        pre_order(root)
        return "".join(res)[1:-1]


test_cases_606 = [([1, 2, 3, 4], "1(2(4))(3)"), ([1, 2, 3, None, 4], "1(2()(4))(3)")]
