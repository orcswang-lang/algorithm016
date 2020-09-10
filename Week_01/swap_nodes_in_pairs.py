# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例:
#
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#  Related Topics 链表
#  👍 614 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        递归方式
        :param head:
        :return:
        """
        # 1. 终止条件：当前没有节点或者只有一个节点，肯定就不需要交换了
        if head is None or head.next is None:
            return head

        # 2. 调用单元
        # 需要交换的两个节点是 head 和 head.next
        firstNode = head
        secondNode = head.next
        # firstNode 连接后面交换完成的子链表
        firstNode.next = self.swapPairs(secondNode.next)
        # secondNode 连接 firstNode
        secondNode.next = firstNode

        # 3. 返回值：返回交换完成的子链表
        # secondNode 变成了头结点
        return secondNode

    def swapPairs2(self, head: ListNode) -> ListNode:
        """
        迭代方式
        :param head:
        :return:
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next

            prev_node.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            prev_node = firstNode
            head = firstNode.next
        return dummy.next

    def swapPairs3(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
# leetcode submit region end(Prohibit modification and deletion)
