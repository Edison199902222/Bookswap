# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
因为这个题目 不需要是leaf 或者从 root出发的 加起来的和
所以从任何一个node出发 只要能得到sum 都可以
所以我们需要两层recrision
第一层是自身出发 然后dfs
然后左孩子出发 右孩子出发
'''
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)

    def dfs(self, root, sum):
        if not root:
            return 0
        sum -= root.val
        if sum == 0:
            return 1 + self.dfs(root.left,sum) + self.dfs(root.right,sum)
        else:
            return self.dfs(root.left,sum) + self.dfs(root.right,sum)



class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.result = 0
        self.helper(root, sum, 0)
        return self.result + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def helper(self, root, target, sums):
        if not root:
            return
        sums += root.val
        if sums == target:
            self.result += 1
        self.helper(root.left, target, sums)
        self.helper(root.right, target, sums)
        return


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TraeeNode
        :type sum: int
        :rtype: int
        """
        # 利用前缀和，和数组一样
        dic = collections.defaultdict(int)
        dic[0] = 1
        self.result = 0
        self.helper(root, dic, 0, sum)
        return self.result

    def helper(self, root, dic, prefix, target):
        if not root:
            return
        prefix += root.val
        # 查当前路径有没有合适的subarray 等于 prefix - target
        count = dic[prefix - target]
        self.result += count
        dic[prefix] += 1
        left = self.helper(root.left, dic, prefix, target)
        right = self.helper(root.right, dic, prefix, target)
        # 回溯
        dic[prefix] -= 1
        return
