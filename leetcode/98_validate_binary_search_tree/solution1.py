from leetcode.utils import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = []
        while root:
            stack.append(root)
            root = root.left

        last_node = stack[-1]
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                if stack[-1].val <= last_node.val:
                    return False
                last_node = stack[-1]

        return True
