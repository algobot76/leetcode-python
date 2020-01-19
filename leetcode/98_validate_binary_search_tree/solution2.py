import sys

from leetcode.utils import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -sys.maxsize - 1, sys.maxsize)

    def helper(self, root: TreeNode, lower: int, upper: int) -> bool:
        if root is None:
            return True
        val = root.val

        if val <= lower or val >= upper:
            return False

        if not self.helper(root.left, lower, val):
            return False
        if not self.helper(root.right, val, upper):
            return False

        return True
