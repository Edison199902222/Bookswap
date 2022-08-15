'''Bfs
运用队列
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queen = []
        queen.append(root)
        while queen:
            length = len(queen)
            current_level = []
            for i in range(length):
                node = queen.pop(0)
                current_level.append(node.val)
                if node.left:
                    queen.append(node.left)
                if node.right:
                    queen.append(node.right)
            result.append(current_level)
        return result
