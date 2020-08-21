# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class BSTIterator:

    def __init__(self, root):
        self.stack = collections.deque()
        self.curr = root

    def next(self):
        """
        @return the next smallest number
        """
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        node = self.curr
        self.curr = self.curr.right

        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return self.stack or self.curr

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
