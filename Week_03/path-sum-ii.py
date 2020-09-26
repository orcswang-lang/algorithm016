# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sumv: int) -> List[List[int]]:
        if not root: return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            node, tmp = stack.pop(0)
            if not node.left and not node.right and sum(tmp) == sumv:
                res.append(tmp)

            if node.left:
                stack.append((node.left, tmp + [node.left.val]))
            if node.right:
                stack.append((node.right, tmp + [node.right.val]))

        return res