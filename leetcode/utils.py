def isBadVersion(version):
    return version % 2 == 0


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
