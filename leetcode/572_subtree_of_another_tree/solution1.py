# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.utils import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tree1 = self.preorder(s)
        tree2 = self.preorder(t)
        return tree1.find(tree2) >= 0

    def preorder(self, t: TreeNode) -> str:
        if t is None:
            return 'null'
        return '#{} {} {}'.format(t.val, self.preorder(t.left),
                                  self.preorder(t.right))
