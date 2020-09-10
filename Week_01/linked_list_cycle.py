# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        Hash = {}
        while head != None:
            if Hash.get(head.next) is not None:
                return True
            Hash[head] = True
            head = head.next
        return False