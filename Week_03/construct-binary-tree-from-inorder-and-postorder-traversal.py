# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left: 'int', in_right: 'int'):
            if in_left > in_right:return None

            val = postorder.pop()
            root = TreeNode(val)

            idx = idx_map[val]

            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx -1)
            return root

        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

    def buildTree1(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if not inorder or not postorder:
            return None
        # 以postorder最后一个元素为根节点建二叉树
        root = TreeNode(postorder[-1])
        inorderIndex = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:inorderIndex], postorder[:inorderIndex])
        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder[inorderIndex:-1])

        return root