# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # 在每一层最后一个node时， 计算下一层的长度
        queue = collections.deque([(root, 1)])
        result = 1
        last_node = root
        while queue:
            node, index = queue.popleft()
            # 有左边的话，编号 放进queue
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
            if node == last_node:
                if len(queue) > 0:
                    result = max(result, queue[-1][1] - queue[0][1] + 1)
                    last_node = queue[-1][0]

        return result