class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


class Solution:

    def max_avg(self, root: TreeNode):
        if not root or not root.children:
            return None
        self.result = [float('-inf'), 0]
        self.dfs(root)
        return self.result[1]

    def dfs(self, root: TreeNode):
        if not root.children:
            self.result = [root.val, 1]

        curr_sum, curr_num = root.val, 1
        for child in root.children:
            child_sum, child_num = self.dfs(child)
            curr_sum += child_sum
            curr_num += child_num

        if curr_sum / curr_num > self.result[0]:
            self.result = [curr_sum / curr_num, root]

        return [curr_sum, curr_num]