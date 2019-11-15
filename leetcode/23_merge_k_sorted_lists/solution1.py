from leetcode.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        return self.helper(lists, 0, len(lists) - 1)

    def merge_two_lists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next

    def helper(self, lists, start, end):
        if start > end:
            return None
        if start == end:
            return lists[start]
        return self.merge_two_lists(
            self.helper(lists, start, (start + end) // 2),
            self.helper(lists, (start + end) // 2 + 1, end))
