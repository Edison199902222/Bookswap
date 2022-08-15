'''
节点数n，树的高度h （极端情况h = n） 时间复杂度：O(n * h) 空间复杂度：额外栈空间 O(h)
'''
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if  len(inorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)
        # postorder  左 -> 右 - > 根， 从中序知道 root 左子树有几个元素后，就可以从postorder 中 头开始拿走元素 这就是左边元素
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index: len(postorder) - 1])
        return root



class Solution(object):
    def buildTree(self, inorder, postorder):
        '''
        后序遍历最后一个是当前层的root
        中序遍历 root 左边是左子树， 右边是右子树
        '''
        self.index = len(postorder) - 1
        self.dic = {}
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.helper(postorder, 0, len(inorder) - 1)

    def helper(self, postorder, start, end):
        if start > end or self.index == - 1:
            return
        root = TreeNode(postorder[self.index])
        # 后序遍历 左 -> 右 -> 根， 从后往前建立root， 所以先建立right
        self.index -= 1
        root_index = self.dic[root.val]
        root.right = self.helper(postorder, root_index + 1, end)
        root.left = self.helper(postorder, start, root_index - 1)
        return root