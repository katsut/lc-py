#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        lst = []
        while (l1 or l2):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            lst.append(v1 + v2)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        sum = 0
        for i, v in enumerate(lst):
            sum = sum + (v * 10 ** i)

        result = None
        for num in str(sum):
            result = ListNode(num, result)

        return result



# @lc code=end

