# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
前序遍历首个节点是root， 左边第一个节点肯定是第二个， 可以通过第二个节点 去后序中找位置 以便确定左边node 的个数
因为后序遍历是 左 右 根， 所以左边第一个节点的位置， 肯定在结束的地方，结束的index 左边都是左node
When the tree is balanced, T(N) = O(N) + 2*T(N/2) = O(NlgN).
In the worst case when the tree is skewed like a linked list, T(N) = O(N) + T(N - 1) = O(N ^ 2).
'''
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None
        # 确认当前层的root
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        # 找到左边node 的个数
        left_length = post.index(pre[1]) + 1
        # 递归两部分，通过左边个数拆分
        root.left = self.constructFromPrePost(pre[1 : 1 + left_length], post[:left_length])
        root.right = self.constructFromPrePost(pre[1 + left_length:], post[left_length : len(post) - 1])
        return root