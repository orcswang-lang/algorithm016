# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """迭代"""
        if not root: return TreeNode(val)

        pos = root
        while pos:
            if val < pos.val:
                if not pos.left:
                    pos.left = TreeNode(val)
                    break
                pos = pos.left
                continue
            if not pos.right:
                pos.right = TreeNode(val)
                break
            pos = pos.right

        return root

    def insertIntoBST1(self, root: TreeNode, val: int) -> TreeNode:
        """递归"""
        if not root: return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root