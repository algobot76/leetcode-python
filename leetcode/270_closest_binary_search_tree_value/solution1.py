# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root, target):
        if root is None:
            return None
        lower = self.get_lower_bound(root, target)
        upper = self.get_upper_bound(root, target)
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val
        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val

    def get_lower_bound(self, root, target):
        if root is None:
            return None

        if target < root.val:
            return self.get_lower_bound(root.left, target)
        lower = self.get_lower_bound(root.right, target)
        return root if lower is None else lower

    def get_upper_bound(self, root, target):
        if root is None:
            return None

        if target >= root.val:
            return self.get_upper_bound(root.right, target)
        upper = self.get_upper_bound(root.left, target)
        return root if upper is None else upper
