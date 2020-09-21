# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """递归"""
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root: TreeNode, res: List[int]):
        if root is None: return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """栈"""
        res, stk = [], []
        stk = []
        while root != None or len(stk) != 0:
            while root != None:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        while stack:  # 栈不为空就循环
            # 左子树中所有最左边的孩子进栈
            while root.left:
                stack.append(root.left)
                root = root.left
            cur = stack.pop()  # 弹出一个左孩子记为当前节点，看它有没有右孩子
            res.append(cur.val)  # 每弹出一次记得记录一下
            if cur.right:  # 如果当前节点有右孩子的话，右孩子进栈，把这个右孩子当作新的根节点
                stack.append(cur.right)
                root = cur.right
        return res

    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)
        return rst

    def inorderTraversal4(self, root: TreeNode) -> List[int]:
        """
        执行超时
        :param root:
        :return:
        """
        res = []
        predecessor = None
        while root != None:
            if root.left != None:
                # predecessor 节点就是当前 root 节点向左走一步，然后一直向右走至无法走为止
                predecessor = root.left
                while predecessor.left != None and predecessor.right != None:
                    predecessor = predecessor.right
                # 让 predecessor 的右指针指向 root，继续遍历左子树
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                # 说明左子树已经访问完了，我们需要断开链接
                else:
                    res.append(root.val)
                    predecessor.right = None
                    root = root.right
            # 如果没有左孩子，则直接访问右孩子
            else:
                res.append(root.val)
                root = root.right
        return res