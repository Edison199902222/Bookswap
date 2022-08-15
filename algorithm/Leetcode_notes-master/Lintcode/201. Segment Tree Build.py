"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """

    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root

        mid = (start + end) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root
'''
构造线段树
首先 判断中止条件
如果发现start 大于 end 我们就无法继续递归
然后建立root
如果发现start == end 的话 那么我们就return root 
如果都没有的话 那么我们继续 递归下去 
'''