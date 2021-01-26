# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parent_x, depth_x = self.helper(root, None, 0, x)
        parent_y, depth_y = self.helper(root, None, 0, y)
        if depth_x == depth_y and parent_x != parent_y:
            return True
        else:
            return False

    def helper(self, root, parent, depth, val):
        if not root:
            return 0, 0
        if root.val == val:
            return parent, depth
        x1, y1 = self.helper(root.left, root, depth + 1, val)
        x2, y2 = self.helper(root.right, root, depth + 1, val)
        if x1 is not 0:
            return x1, y1
        if x2 is not 0:
            return x2, y2
        return 0,0



'''
这道题需要注意的是 
最后也需要return 0，0 
因为在每一层递归的时候 我们需要用两个变量得到左子树的parent 跟 depth 
如果最后不return0，0的话 那么 如果左子树没有找到我们想要的val 那么只会return none
然后我们又需要返回 两个变量的值 但这时候 只有一个变量 所以会报错

题目的总体思路就是 
建立一个function 目的是 为了找 一个val 的parent 跟 深度 
然后 我们用这个function 去找 x跟y的parent  还有 深度
最后 如果 x 跟 y的深度一样 parent 不一样 return true
不然的话 return false
'''
if __name__ == "__main__":
    solution = Solution2()
    x1 = TreeNode(1)
    x2 = TreeNode(2)
    x3 = TreeNode(3)
    x4 = TreeNode(4)
    x5 =  TreeNode(5)
    x1.left = x2
    x1.right = x3
    x2.right = x4
    x3.right = x5
    print(solution.isCousins(x1, 5, 4))