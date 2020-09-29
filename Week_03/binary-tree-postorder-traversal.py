# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """递归"""
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)
        return res

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """迭代"""
        if not root: return []

        res, stack, prev = [], [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """迭代"""
        if not root: return []

        ans, stack = [], [root]

        while stack:
            node = stack.pop()
            if node:
                # 如果节点不为空，
                # 当前节点重新入栈
                stack.append(node)
                # 这里添加 None，为了后面处理数据，
                # 标记左右子节点访问结束，可处理当前节点
                stack.append(None)
                # 这里先将右子节点入栈
                if node.right: stack.append(node.right)
                # 再将左子节点入栈
                if node.left: stack.append(node.left)
            else:
                node = stack.pop()
                ans.append(node.val)

        return ans