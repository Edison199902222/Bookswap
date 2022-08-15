# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        self.count = 0
        self.helper(root, distance)
        return self.count

    def helper(self, root, distance):
        if not root:
            return {}
        if not root.left and not root.right:
            # 找到叶子，返回字典
            return {root: 1}
        # 找到左右两边的叶子
        left = self.helper(root.left, distance)
        right = self.helper(root.right, distance)

        delete = set()
        # 如果都有的话，遍历查找
        # 并且如果发现有一个单独的叶子节点距离就超过distance的话，放进delete
        for left_node in left:
            if left[left_node] >= distance:
                delete.add(left_node)
                continue
            for right_node in right:
                if right[right_node] >= distance:
                    delete.add(right_node)
                    continue
                if left[left_node] + right[right_node] <= distance:
                    self.count += 1
        # 把左右两边符合条件的叶子节点放进counter中
        new_counter = {}
        for left_node in left:
            if left_node not in delete:
                new_counter[left_node] = left[left_node] + 1
        for right_node in right:
            if right_node not in delete:
                new_counter[right_node] = right[right_node] + 1
        return new_counter





