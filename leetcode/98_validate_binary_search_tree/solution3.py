import collections
import sys

from leetcode.utils import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = collections.deque([(root, -sys.maxsize - 1, sys.maxsize)])
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue

            if root.val <= lower or root.val >= upper:
                return False

            stack.append((root.left, lower, root.val))
            stack.append((root.right, root.val, upper))

        return True
