def isBadVersion(version):
    return version % 2 == 0


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
