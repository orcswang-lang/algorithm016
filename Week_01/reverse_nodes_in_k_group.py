# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 反转 k 个元素，返回反转后的头、尾节点。
        def revrese(head, k):
            pre, cur = None, head
            for _ in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            return pre, head

        pre = dummy = ListNode(0)
        dummy.next = head
        while pre.next:
            # 判断剩余节点个数是否有 k 个，若没有直接返回。
            # 另一个目的是将 cur 定位到 k+1 个节点的位置，方便后续的拼接。
            cur = pre.next
            for _ in range(k):
                if not cur:
                    return dummy.next
                cur = cur.next
            # 将 pre 连接已经反转好的元素，顺便移动 pre 的位置。
            pre.next, pre = revrese(pre.next, k)
            # 拼接剩余元素，否则无法继续迭代。
            pre.next = cur

        return dummy.next