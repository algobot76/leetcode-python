import collections
import sys

from leetcode.utils import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = collections.deque()
        lower = -sys.maxsize - 1
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= lower:
                return False
            lower = root.val
            root = root.right

        return True
