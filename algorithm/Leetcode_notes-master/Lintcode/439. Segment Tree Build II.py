"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        start = 0
        end = len(A) - 1
        return self.build_tree(start, end, A)

    def build_tree(self,start, end, A):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, A[start])
        if start == end:
            return root
        mid = (start + end) // 2
        root.left = self.build_tree(start, mid, A)
        root.right = self.build_tree(mid + 1, end, A)
        root.max = max(root.left.max, root.right.max, root.max)
        return root
'''
还是递归
先判断什么时候中止
然后递归建造左右孩子 
建造完 跟左孩子 右孩子 还有自己 比较谁是max
'''