
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
dfs
res储存root
需要有一个level 因为只有level跟res长度相等的时候才能加东西
比如左右都有孩子的话，右边加完东西之后 左边就不能加东西了 用level就能保证左边加不了东西
'''

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        self.res = []
        self.dfs(root,0)
        return self.res


    def dfs(self,root,level):
        if not root:return
        if len(self.res) == level:
            self.res.append(root.val)
        self.dfs(root.right,level+1)
        self.dfs(root.left, level+1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

