# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """DFS"""
        if not t1:return t2
        if not t2:return t1
        m = TreeNode(t1.val + t2.val)
        m.left = self.mergeTrees(t1.left, t2.left)
        m.right = self.mergeTrees(t1.right, t2.right)
        return m

    def mergeTrees1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not (t1 and t2):
            return t1 or t2
        queue1, queue2 = collections.deque([t1]), collections.deque([t2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return t1

    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2: return t1 or t2
        s = [(t1, t2)]
        while s:
            n1, n2 = s.pop()
            if not n2: continue
            n1.val += n2.val
            if not n1.left and n2.left: n1.left = TreeNode(0)
            if not n1.right and n2.right: n1.right = TreeNode(0)
            s.append((n1.right, n2.right))
            s.append((n1.left, n2.left))
        return t1