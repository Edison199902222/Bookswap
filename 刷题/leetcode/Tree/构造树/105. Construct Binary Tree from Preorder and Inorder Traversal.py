# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
前序加中序
前序第一个结点可以知道root是什么
然后定位root在inorder之中 左边就是left 右边就是right
节点数n，树的高度h （极端情况h = n） 时间复杂度：O(n * h) 空间复杂度：额外栈空间 O(h)
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        中序遍历确定root 位置后， 左边是左子树， 右边是右子树
        前序遍历首位可以确定当前层的root
        '''
        if len(inorder) == 0:return None
        root = TreeNode(preorder[0])
        # 通过确定root的 index 知道 root左子树还有几个元素
        root_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: 1 + root_index],inorder[:root_index])
        root.right = self.buildTree(preorder[1 + root_index:],inorder[root_index + 1:])
        return root


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 根据inoder 来划分 左右子树的长度
        # 得到左 右子树的长度后， 可以跟preoder 来建立左子树， 再建立右子树
        # 记录preoder 数组中遍历到哪
        self.index = 0
        self.dic = {}
        # inorder 的index 放进 dic
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.helper(preorder, 0, len(preorder) - 1)

    def helper(self, preorder, start, end):
        # start 和 end 是划分 左右子树
        if start > end or self.index == len(preorder):
            return
            # 得到当前层的root
        root = TreeNode(preorder[self.index])
        self.index += 1
        # 划分左 右子树的长度
        root_index = self.dic[root.val]
        root.left = self.helper(preorder, start, root_index - 1)
        root.right = self.helper(preorder, root_index + 1, end)
        return root

