# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.utils import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        sum_ = int(num1) + int(num2)
        dummy = ListNode(0)
        curr = dummy
        for n in str(sum_)[::-1]:
            curr.next = ListNode(int(n))
            curr = curr.next
        return dummy.next
